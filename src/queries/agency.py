from pyspark.sql.functions import (
    avg, col, count, countDistinct, desc, explode, lag, min as spark_min,
    round as spark_round, row_number, split, sum as spark_sum, when,
)
from pyspark.sql.window import Window

from src.queries import LATEST_FULL_YEAR
from src.utils import save_result


def rising_stars(data: dict, out_dir: str) -> None:
    actors = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
        .distinct()
    )
    basics_with_year = data["title_basics"].filter(col("startYear").isNotNull())
    significant_ratings = data["title_ratings"].filter(col("numVotes") >= 50000)
    significant = (
        actors.join(basics_with_year, "tconst")
        .join(significant_ratings, "tconst")
    )
    first_signif = (
        significant.groupBy("nconst")
        .agg(
            spark_min("startYear").alias("first_significant_year"),
            count("tconst").alias("significant_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
        )
        .filter(col("first_significant_year") >= LATEST_FULL_YEAR - 5)
        .filter(col("significant_count") >= 3)
        .filter(col("avg_rating") >= 7.0)
    )
    w = Window.orderBy(desc("avg_rating"), desc("significant_count"))
    result = (
        first_signif.withColumn("rank", row_number().over(w))
        .join(data["name_basics"], "nconst")
        .select(
            "rank", "primaryName",
            "first_significant_year", "significant_count", "avg_rating",
        )
        .orderBy("rank")
        .limit(50)
    )
    save_result(result, out_dir, "rising_stars")


def genre_profile(data: dict, out_dir: str) -> None:
    actor_films = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
        .distinct()
        .join(
            data["title_basics"]
            .filter(col("genres").isNotNull())
            .filter(col("titleType").isin("movie", "tvSeries", "tvMiniSeries", "tvMovie")),
            "tconst",
        )
        .select("nconst", "tconst", "genres")
    ).cache()
    actor_totals = (
        actor_films.groupBy("nconst")
        .agg(countDistinct("tconst").alias("total_titles"))
    )
    actor_genre = (
        actor_films
        .withColumn("genre", explode(split(col("genres"), ",")))
        .groupBy("nconst", "genre")
        .agg(count("tconst").alias("genre_count"))
    )
    w_total_tags = Window.partitionBy("nconst")
    w_top = Window.partitionBy("nconst").orderBy(desc("genre_count"))
    enriched = (
        actor_genre.withColumn("total_tags", spark_sum("genre_count").over(w_total_tags))
        .withColumn("share", col("genre_count") / col("total_tags"))
        .withColumn("genre_rank", row_number().over(w_top))
    )
    dominant = (
        enriched.filter(col("genre_rank") == 1)
        .join(actor_totals, "nconst")
        .filter(col("total_titles") >= 10)
        .withColumn(
            "classification",
            when(col("share") > 0.6, "specialist")
            .when(col("share") < 0.3, "utility")
            .otherwise("mixed"),
        )
        .filter(col("classification").isin("specialist", "utility"))
    )
    result = (
        dominant.join(data["name_basics"], "nconst")
        .select(
            "primaryName", "total_titles",
            col("genre").alias("dominant_genre"),
            spark_round(col("share") * 100, 1).alias("dominant_share_pct"),
            "classification",
        )
        .orderBy(desc("total_titles"), desc("dominant_share_pct"))
        .limit(200)
    )
    save_result(result, out_dir, "genre_profile")
    actor_films.unpersist()


def co_star_chemistry(data: dict, out_dir: str) -> None:
    movie_actors = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
        .distinct()
        .join(data["title_basics"].filter(col("titleType") == "movie"), "tconst")
        .join(data["title_ratings"], "tconst")
        .select("tconst", "nconst", "averageRating")
    ).cache()
    actor_totals = (
        movie_actors.groupBy("nconst")
        .agg(
            spark_sum("averageRating").alias("rating_sum"),
            count("tconst").alias("film_count"),
        )
    )
    a1 = movie_actors.alias("a1")
    a2 = movie_actors.alias("a2")
    joint_stats = (
        a1.join(
            a2,
            (col("a1.tconst") == col("a2.tconst"))
            & (col("a1.nconst") < col("a2.nconst")),
        )
        .groupBy(
            col("a1.nconst").alias("actor1"),
            col("a2.nconst").alias("actor2"),
        )
        .agg(
            count("*").alias("joint_count"),
            spark_sum(col("a1.averageRating")).alias("joint_rating_sum"),
            spark_round(avg(col("a1.averageRating")), 2).alias("joint_avg"),
        )
        .filter(col("joint_count") >= 5)
    )
    t1 = actor_totals.select(
        col("nconst").alias("a_id1"),
        col("rating_sum").alias("rating_sum1"),
        col("film_count").alias("film_count1"),
    )
    t2 = actor_totals.select(
        col("nconst").alias("a_id2"),
        col("rating_sum").alias("rating_sum2"),
        col("film_count").alias("film_count2"),
    )
    enriched = (
        joint_stats.join(t1, col("actor1") == col("a_id1"))
        .join(t2, col("actor2") == col("a_id2"))
        .withColumn("solo_count1", col("film_count1") - col("joint_count"))
        .withColumn("solo_count2", col("film_count2") - col("joint_count"))
        .filter(col("solo_count1") >= 10)
        .filter(col("solo_count2") >= 10)
        .withColumn(
            "solo_avg1",
            spark_round(
                (col("rating_sum1") - col("joint_rating_sum")) / col("solo_count1"), 2
            ),
        )
        .withColumn(
            "solo_avg2",
            spark_round(
                (col("rating_sum2") - col("joint_rating_sum")) / col("solo_count2"), 2
            ),
        )
        .filter(col("joint_avg") > col("solo_avg1"))
        .filter(col("joint_avg") > col("solo_avg2"))
        .withColumn(
            "premium",
            spark_round(
                col("joint_avg") - ((col("solo_avg1") + col("solo_avg2")) / 2), 2
            ),
        )
    )
    n1 = data["name_basics"].select(
        col("nconst").alias("n1"), col("primaryName").alias("name1")
    )
    n2 = data["name_basics"].select(
        col("nconst").alias("n2"), col("primaryName").alias("name2")
    )
    result = (
        enriched.join(n1, col("actor1") == col("n1"))
        .join(n2, col("actor2") == col("n2"))
        .select(
            "name1", "name2",
            "joint_count", "joint_avg",
            "solo_avg1", "solo_avg2", "premium",
        )
        .orderBy(desc("premium"))
        .limit(50)
    )
    save_result(result, out_dir, "co_star_chemistry")
    movie_actors.unpersist()


def signature_collaborations(data: dict, out_dir: str) -> None:
    qualifying_titles = (
        data["title_basics"]
        .filter(col("titleType").isin("movie", "tvMiniSeries"))
        .select("tconst")
    )
    directors = (
        data["title_crew"]
        .filter(col("directors").isNotNull())
        .join(qualifying_titles, "tconst", "left_semi")
        .withColumn("director_id", explode(split(col("directors"), ",")))
        .select("tconst", "director_id")
    ).cache()
    actors = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", col("nconst").alias("actor_id"))
        .distinct()
        .join(qualifying_titles, "tconst", "left_semi")
    )
    rated = data["title_ratings"]
    director_actor = directors.join(actors, "tconst").join(rated, "tconst")
    director_overall = (
        directors.join(rated, "tconst")
        .groupBy("director_id")
        .agg(
            spark_round(avg("averageRating"), 2).alias("director_avg"),
            count("tconst").alias("director_titles"),
        )
        .filter(col("director_titles") >= 5)
    )
    pair_stats = (
        director_actor.groupBy("director_id", "actor_id")
        .agg(
            count("tconst").alias("collab_count"),
            spark_round(avg("averageRating"), 2).alias("pair_avg"),
        )
        .filter(col("collab_count") >= 5)
    )
    enriched = (
        pair_stats.join(director_overall, "director_id")
        .filter(col("pair_avg") > col("director_avg"))
        .withColumn(
            "uplift", spark_round(col("pair_avg") - col("director_avg"), 2)
        )
    )
    nd = data["name_basics"].select(
        col("nconst").alias("d_id"), col("primaryName").alias("director_name")
    )
    na = data["name_basics"].select(
        col("nconst").alias("a_id"), col("primaryName").alias("actor_name")
    )
    result = (
        enriched.join(nd, col("director_id") == col("d_id"))
        .join(na, col("actor_id") == col("a_id"))
        .select(
            "director_name", "actor_name",
            "collab_count", "pair_avg", "director_avg", "uplift",
        )
        .orderBy(desc("uplift"), desc("collab_count"))
        .limit(50)
    )
    save_result(result, out_dir, "signature_collaborations")
    directors.unpersist()


def comeback_actors(data: dict, out_dir: str) -> None:
    actor_titles = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
        .distinct()
        .join(
            data["title_basics"]
            .filter(col("startYear").isNotNull())
            .filter(col("titleType").isin("movie", "tvSeries", "tvMiniSeries", "tvMovie")),
            "tconst",
        )
        .join(data["title_ratings"], "tconst")
        .select("nconst", col("startYear").alias("year"), "averageRating")
    )
    bucketed = actor_titles.withColumn(
        "era",
        when(col("year") >= LATEST_FULL_YEAR - 4, "recent").otherwise("past"),
    )
    pivoted = (
        bucketed.groupBy("nconst")
        .pivot("era", ["recent", "past"])
        .agg(
            count("year").alias("count"),
            spark_round(avg("averageRating"), 2).alias("avg"),
        )
        .filter(col("recent_count").isNotNull() & col("past_count").isNotNull())
        .filter((col("recent_count") + col("past_count")) >= 10)
        .filter(col("recent_count") >= 3)
        .filter(col("past_count") >= 5)
        .withColumn(
            "improvement", spark_round(col("recent_avg") - col("past_avg"), 2)
        )
        .filter(col("improvement") >= 1.0)
    )
    result = (
        pivoted.join(data["name_basics"], "nconst")
        .select(
            "primaryName",
            col("past_count").alias("past_titles"), "past_avg",
            col("recent_count").alias("recent_titles"), "recent_avg",
            "improvement",
        )
        .orderBy(desc("improvement"))
        .limit(50)
    )
    save_result(result, out_dir, "comeback_actors")


def typecast_decline(data: dict, out_dir: str) -> None:
    actor_films = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
        .distinct()
        .join(
            data["title_basics"]
            .filter(col("genres").isNotNull())
            .filter(col("startYear").isNotNull())
            .filter(col("titleType").isin("movie", "tvSeries", "tvMiniSeries", "tvMovie")),
            "tconst",
        )
        .join(data["title_ratings"], "tconst")
        .select("nconst", "tconst", "genres",
                col("startYear").alias("year"), "averageRating")
    ).cache()
    actor_totals = (
        actor_films.groupBy("nconst")
        .agg(countDistinct("tconst").alias("total_titles"))
    )
    actor_genre_year = (
        actor_films
        .withColumn("genre", explode(split(col("genres"), ",")))
        .select("nconst", "genre", "year", "averageRating")
    ).cache()
    by_actor_genre = (
        actor_genre_year.groupBy("nconst", "genre")
        .agg(count("year").alias("genre_count"))
    )
    w_total_tags = Window.partitionBy("nconst")
    w_rank = Window.partitionBy("nconst").orderBy(desc("genre_count"))
    dominant = (
        by_actor_genre.withColumn(
            "total_tags", spark_sum("genre_count").over(w_total_tags)
        )
        .withColumn("share", col("genre_count") / col("total_tags"))
        .withColumn("genre_rank", row_number().over(w_rank))
        .filter(col("genre_rank") == 1)
        .join(actor_totals, "nconst")
        .filter(col("total_titles") >= 10)
        .filter(col("share") > 0.7)
        .select(
            "nconst",
            col("genre").alias("dominant_genre"),
            "total_titles",
            "share",
        )
    )
    actor_dominant = actor_genre_year.alias("a").join(
        dominant, "nconst"
    ).filter(col("a.genre") == col("dominant_genre"))

    yearly = (
        actor_dominant.groupBy(
            "nconst", "year", "dominant_genre", "share", "total_titles"
        )
        .agg(spark_round(avg(col("a.averageRating")), 2).alias("year_avg"))
    )
    w_year = Window.partitionBy("nconst").orderBy("year")
    yearly = yearly.withColumn(
        "prev_year_avg", lag("year_avg").over(w_year)
    ).withColumn("yoy_delta", col("year_avg") - col("prev_year_avg"))
    declining = (
        yearly.groupBy("nconst", "dominant_genre", "share", "total_titles")
        .agg(
            spark_round(avg("yoy_delta"), 2).alias("avg_yoy_change"),
            count("year").alias("active_years"),
        )
        .filter(col("active_years") >= 3)
        .filter(col("avg_yoy_change") < 0)
    )
    result = (
        declining.join(data["name_basics"], "nconst")
        .select(
            "primaryName",
            "dominant_genre",
            spark_round(col("share") * 100, 1).alias("dominant_share_pct"),
            "total_titles",
            "avg_yoy_change",
        )
        .orderBy("avg_yoy_change")
        .limit(50)
    )
    save_result(result, out_dir, "typecast_decline")
    actor_genre_year.unpersist()
    actor_films.unpersist()


def run(data: dict, output_path: str) -> None:
    print("\n=== AGENCY QUERIES ===")
    out = f"{output_path}/agency"
    rising_stars(data, out)
    genre_profile(data, out)
    co_star_chemistry(data, out)
    signature_collaborations(data, out)
    comeback_actors(data, out)
    typecast_decline(data, out)
