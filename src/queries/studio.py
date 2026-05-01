from pyspark.sql.functions import (
    avg, col, count, desc, explode, lag, max as spark_max,
    percentile_approx, rank, round as spark_round, row_number,
    split, sum as spark_sum, when,
)
from pyspark.sql.window import Window

from src.queries import LATEST_FULL_YEAR
from src.utils import save_result


def bankable_directors(data: dict, out_dir: str) -> None:
    directors = (
        data["title_crew"]
        .filter(col("directors").isNotNull())
        .withColumn("director_id", explode(split(col("directors"), ",")))
        .select("tconst", "director_id")
    )
    stats = (
        directors.join(data["title_ratings"], "tconst")
        .groupBy("director_id")
        .agg(
            count("tconst").alias("title_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
            spark_round(avg("numVotes"), 0).alias("avg_votes"),
        )
        .filter(col("title_count") >= 10)
        .filter(col("avg_rating") >= 7.0)
        .filter(col("avg_votes") >= 50000)
    )
    result = (
        stats.join(
            data["name_basics"],
            stats["director_id"] == data["name_basics"]["nconst"],
        )
        .select("primaryName", "title_count", "avg_rating", "avg_votes")
        .orderBy(desc("avg_rating"), desc("avg_votes"))
        .limit(50)
    )
    save_result(result, out_dir, "bankable_directors")


def genre_momentum(data: dict, out_dir: str) -> None:
    recent_start = LATEST_FULL_YEAR - 9
    prior_start = LATEST_FULL_YEAR - 19
    prior_end = LATEST_FULL_YEAR - 10

    movies = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .filter(col("startYear").isNotNull())
        .filter(col("genres").isNotNull())
        .withColumn("genre", explode(split(col("genres"), ",")))
    )
    rated = movies.join(data["title_ratings"], "tconst")
    bucketed = (
        rated.withColumn(
            "era",
            when(col("startYear").between(recent_start, LATEST_FULL_YEAR), "recent")
            .when(col("startYear").between(prior_start, prior_end), "prior"),
        )
        .filter(col("era").isNotNull())
        .groupBy("genre", "era")
        .agg(
            count("tconst").alias("title_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
        )
    )
    pivoted = (
        bucketed.groupBy("genre")
        .pivot("era", ["recent", "prior"])
        .agg(
            spark_max("title_count").alias("count"),
            spark_max("avg_rating").alias("rating"),
        )
        .filter(col("recent_count").isNotNull() & col("prior_count").isNotNull())
        .filter(col("prior_count") >= 50)
    )
    result = (
        pivoted.withColumn(
            "count_growth_pct",
            spark_round(
                (col("recent_count") - col("prior_count")) / col("prior_count") * 100, 1
            ),
        )
        .withColumn(
            "rating_delta", spark_round(col("recent_rating") - col("prior_rating"), 2)
        )
        .withColumn(
            "momentum_score",
            spark_round(col("count_growth_pct") / 10 + col("rating_delta") * 5, 2),
        )
        .select(
            "genre", "recent_count", "prior_count", "count_growth_pct",
            "recent_rating", "prior_rating", "rating_delta", "momentum_score",
        )
        .orderBy(desc("momentum_score"))
    )
    save_result(result, out_dir, "genre_momentum")


def optimal_runtime_band(data: dict, out_dir: str) -> None:
    movies = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .filter(col("runtimeMinutes").isNotNull())
        .filter(col("genres").isNotNull())
        .withColumn("genre", explode(split(col("genres"), ",")))
        .withColumn(
            "runtime_band",
            when(col("runtimeMinutes") < 60, "<60")
            .when(col("runtimeMinutes") < 90, "60-90")
            .when(col("runtimeMinutes") < 120, "90-120")
            .when(col("runtimeMinutes") < 150, "120-150")
            .otherwise("150+"),
        )
    )
    rated = movies.join(data["title_ratings"], "tconst").filter(col("numVotes") >= 1000)
    band_stats = (
        rated.groupBy("genre", "runtime_band")
        .agg(
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
            count("tconst").alias("movie_count"),
        )
        .filter(col("movie_count") >= 50)
    )
    w = Window.partitionBy("genre").orderBy(desc("avg_rating"))
    result = (
        band_stats.withColumn("rank_in_genre", rank().over(w))
        .select("genre", "rank_in_genre", "runtime_band", "avg_rating", "movie_count")
        .orderBy("genre", "rank_in_genre")
    )
    save_result(result, out_dir, "optimal_runtime_band")


def franchise_anchor_actors(data: dict, out_dir: str) -> None:
    actors = (
        data["title_principals"]
        .filter(col("category").isin("actor", "actress"))
        .select("tconst", "nconst")
    )
    stats = (
        actors.join(data["title_ratings"], "tconst")
        .groupBy("nconst")
        .agg(
            count("tconst").alias("title_count"),
            spark_round(
                spark_sum(col("averageRating") * col("numVotes"))
                / spark_sum(col("numVotes")),
                2,
            ).alias("weighted_rating"),
            spark_sum("numVotes").alias("total_votes"),
        )
        .filter(col("title_count") >= 20)
        .filter(col("weighted_rating") >= 7.0)
    )
    w = Window.orderBy(desc("weighted_rating"), desc("total_votes"))
    result = (
        stats.withColumn("rank", row_number().over(w))
        .join(data["name_basics"], "nconst")
        .select("rank", "primaryName", "title_count", "weighted_rating", "total_votes")
        .orderBy("rank")
        .limit(100)
    )
    save_result(result, out_dir, "franchise_anchor_actors")


def director_consistency_vs_variance(data: dict, out_dir: str) -> None:
    directors = (
        data["title_crew"]
        .filter(col("directors").isNotNull())
        .withColumn("director_id", explode(split(col("directors"), ",")))
        .select("tconst", "director_id")
    )
    rated = directors.join(data["title_ratings"], "tconst")
    stats = (
        rated.groupBy("director_id")
        .agg(
            count("tconst").alias("title_count"),
            spark_max("averageRating").alias("max_rating"),
            spark_round(percentile_approx("averageRating", 0.5), 2).alias("median_rating"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
        )
        .filter(col("title_count") >= 5)
        .withColumn(
            "variance_range", spark_round(col("max_rating") - col("median_rating"), 2)
        )
    )
    w = Window.orderBy(desc("variance_range"), desc("max_rating"))
    result = (
        stats.withColumn("rank", row_number().over(w))
        .join(
            data["name_basics"],
            stats["director_id"] == data["name_basics"]["nconst"],
        )
        .select(
            "rank", "primaryName", "title_count",
            "max_rating", "median_rating", "avg_rating", "variance_range",
        )
        .orderBy("rank")
        .limit(100)
    )
    save_result(result, out_dir, "director_consistency_vs_variance")


def oversaturated_release_years(data: dict, out_dir: str) -> None:
    movies = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .filter(col("startYear").isNotNull())
        .filter(col("startYear").between(1950, LATEST_FULL_YEAR))
        .filter(col("genres").isNotNull())
        .withColumn("genre", explode(split(col("genres"), ",")))
    )
    rated = movies.join(data["title_ratings"], "tconst")
    yearly = (
        rated.groupBy("genre", "startYear")
        .agg(
            count("tconst").alias("title_count"),
            spark_round(percentile_approx("averageRating", 0.5), 2).alias("median_rating"),
        )
    )
    w = Window.partitionBy("genre").orderBy("startYear")
    result = (
        yearly.withColumn("prev_count", lag("title_count").over(w))
        .withColumn("prev_median", lag("median_rating").over(w))
        .withColumn(
            "count_yoy_pct",
            spark_round(
                (col("title_count") - col("prev_count")) / col("prev_count") * 100, 1
            ),
        )
        .withColumn(
            "median_yoy", spark_round(col("median_rating") - col("prev_median"), 2)
        )
        .withColumn(
            "flag",
            when(
                (col("count_yoy_pct") > 30) & (col("median_yoy") < 0), "oversaturated"
            ).when(
                (col("count_yoy_pct") < -10) & (col("median_yoy") > 0), "opportunity"
            ),
        )
        .filter(col("flag").isNotNull())
        .select(
            "genre", "startYear",
            "title_count", "count_yoy_pct",
            "median_rating", "median_yoy", "flag",
        )
        .orderBy("genre", "startYear")
    )
    save_result(result, out_dir, "oversaturated_release_years")


def run(data: dict, output_path: str) -> None:
    print("\n=== STUDIO QUERIES ===")
    out = f"{output_path}/studio"
    bankable_directors(data, out)
    genre_momentum(data, out)
    optimal_runtime_band(data, out)
    franchise_anchor_actors(data, out)
    director_consistency_vs_variance(data, out)
    oversaturated_release_years(data, out)
