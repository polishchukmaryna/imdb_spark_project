from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    avg, col, count, countDistinct, desc, explode,
    max as spark_max, min as spark_min, round as spark_round,
    row_number, split, stddev,
)
from pyspark.sql.window import Window

from src.utils import save_result


def _season_ratings(data: dict) -> DataFrame:
    return (
        data["title_episode"]
        .filter(col("seasonNumber").isNotNull())
        .filter(col("parentTconst").isNotNull())
        .join(data["title_ratings"], "tconst")
        .groupBy("parentTconst", "seasonNumber")
        .agg(spark_round(avg("averageRating"), 2).alias("season_avg"))
    )


def hidden_gems(data: dict, out_dir: str) -> None:
    movies = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .filter(col("genres").isNotNull())
        .join(
            data["title_ratings"]
            .filter(col("averageRating") >= 8.0)
            .filter(col("numVotes").between(1000, 50000)),
            "tconst",
        )
        .withColumn("genre", explode(split(col("genres"), ",")))
    )
    w = Window.partitionBy("genre").orderBy(desc("averageRating"), desc("numVotes"))
    result = (
        movies.withColumn("rank_in_genre", row_number().over(w))
        .filter(col("rank_in_genre") <= 10)
        .select(
            "genre", "rank_in_genre", "primaryTitle", "startYear",
            "averageRating", "numVotes",
        )
        .orderBy("genre", "rank_in_genre")
    )
    save_result(result, out_dir, "hidden_gems")


def renewal_risk(data: dict, out_dir: str) -> None:
    season_ratings = _season_ratings(data)
    w_per_series = Window.partitionBy("parentTconst")
    w_recent = Window.partitionBy("parentTconst").orderBy(desc("seasonNumber"))
    enriched = (
        season_ratings
        .withColumn("total_seasons", spark_max("seasonNumber").over(w_per_series))
        .withColumn("peak_rating", spark_max("season_avg").over(w_per_series))
        .withColumn("season_recency", row_number().over(w_recent))
        .filter(col("total_seasons") >= 3)
        .filter(col("season_recency") == 1)
        .filter(col("peak_rating") >= 7.5)
        .filter(col("season_avg") >= 4.0)
        .withColumn(
            "drop_from_peak", spark_round(col("peak_rating") - col("season_avg"), 2)
        )
        .filter(col("drop_from_peak").between(0.5, 2.5))
    )
    series_basics = data["title_basics"].filter(col("titleType") == "tvSeries")
    result = (
        enriched.join(
            series_basics,
            enriched["parentTconst"] == series_basics["tconst"],
        )
        .select(
            "primaryTitle", "total_seasons", "seasonNumber",
            "peak_rating", "season_avg", "drop_from_peak",
        )
        .orderBy(desc("drop_from_peak"))
        .limit(100)
    )
    save_result(result, out_dir, "renewal_risk")


def binge_classics(data: dict, out_dir: str) -> None:
    season_ratings = _season_ratings(data)
    series_stats = (
        season_ratings.groupBy("parentTconst")
        .agg(
            count("seasonNumber").alias("season_count"),
            spark_min("season_avg").alias("min_season_rating"),
            spark_round(avg("season_avg"), 2).alias("avg_season_rating"),
        )
        .filter(col("season_count") >= 3)
        .filter(col("min_season_rating") >= 7.5)
    )
    completed_series = (
        data["title_basics"]
        .filter(col("titleType") == "tvSeries")
        .filter(col("endYear").isNotNull())
        .join(data["title_ratings"].filter(col("numVotes") >= 10000), "tconst")
    )
    result = (
        series_stats.join(
            completed_series,
            series_stats["parentTconst"] == completed_series["tconst"],
        )
        .select(
            "primaryTitle", "startYear", "endYear",
            "season_count", "min_season_rating", "avg_season_rating", "numVotes",
        )
        .orderBy(desc("min_season_rating"), desc("numVotes"))
        .limit(100)
    )
    save_result(result, out_dir, "binge_classics")


def dead_weight(data: dict, out_dir: str) -> None:
    movies = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .filter(col("genres").isNotNull())
        .join(
            data["title_ratings"]
            .filter(col("numVotes") >= 10000)
            .filter(col("averageRating") < 5.5),
            "tconst",
        )
        .withColumn("genre", explode(split(col("genres"), ",")))
    )
    result = (
        movies.select(
            "genre", "primaryTitle", "startYear", "averageRating", "numVotes"
        )
        .orderBy("genre", "averageRating", "numVotes")
        .limit(500)
    )
    save_result(result, out_dir, "dead_weight")


def episode_consistency(data: dict, out_dir: str) -> None:
    episode_ratings = (
        data["title_episode"]
        .filter(col("parentTconst").isNotNull())
        .join(data["title_ratings"].filter(col("numVotes") >= 100), "tconst")
    )
    series_stats = (
        episode_ratings.groupBy("parentTconst")
        .agg(
            count("tconst").alias("episode_count"),
            spark_round(avg("averageRating"), 2).alias("mean_rating"),
            spark_round(stddev("averageRating"), 2).alias("rating_stddev"),
            spark_round(avg("numVotes"), 0).alias("avg_votes_per_episode"),
        )
        .filter(col("episode_count") >= 30)
        .filter(col("mean_rating") >= 7.0)
        .filter(col("avg_votes_per_episode") >= 1000)
    )
    series_basics = data["title_basics"].filter(col("titleType") == "tvSeries")
    enriched = series_stats.join(
        series_basics,
        series_stats["parentTconst"] == series_basics["tconst"],
    )
    w = Window.orderBy(col("rating_stddev").asc(), desc("mean_rating"))
    result = (
        enriched.withColumn("bingeability_rank", row_number().over(w))
        .select(
            "bingeability_rank", "primaryTitle",
            "episode_count", "mean_rating", "rating_stddev", "avg_votes_per_episode",
        )
        .orderBy("bingeability_rank")
        .limit(100)
    )
    save_result(result, out_dir, "episode_consistency")


def globally_portable_titles(data: dict, out_dir: str) -> None:
    region_count = (
        data["title_akas"]
        .filter(col("region").isNotNull())
        .groupBy("titleId")
        .agg(countDistinct("region").alias("region_count"))
        .filter(col("region_count") >= 10)
    )
    qualifying_basics = data["title_basics"].filter(
        col("titleType").isin("movie", "tvSeries")
    )
    qualifying_ratings = data["title_ratings"].filter(col("numVotes") >= 1000)
    enriched = (
        region_count.join(
            qualifying_basics,
            region_count["titleId"] == qualifying_basics["tconst"],
        )
        .join(qualifying_ratings, "tconst")
    )
    w = Window.orderBy(desc("region_count"), desc("averageRating"))
    result = (
        enriched.withColumn("rank", row_number().over(w))
        .select(
            "rank", "primaryTitle", "titleType", "startYear",
            "region_count", "averageRating", "numVotes",
        )
        .orderBy("rank")
        .limit(100)
    )
    save_result(result, out_dir, "globally_portable_titles")


def run(data: dict, output_path: str) -> None:
    print("\n=== STREAMING QUERIES ===")
    out = f"{output_path}/streaming"
    hidden_gems(data, out)
    renewal_risk(data, out)
    binge_classics(data, out)
    dead_weight(data, out)
    episode_consistency(data, out)
    globally_portable_titles(data, out)
