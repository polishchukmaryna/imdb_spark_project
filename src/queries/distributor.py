from pyspark.sql.functions import (
    avg, col, count, countDistinct, dense_rank, desc, explode,
    log10, max as spark_max, rank, round as spark_round, row_number,
    split, sum as spark_sum, when,
)
from pyspark.sql.window import Window

from src.queries import LATEST_FULL_YEAR
from src.utils import save_result


def ua_licensing_backlog(data: dict, out_dir: str) -> None:
    candidate = (
        data["title_basics"]
        .filter(col("titleType") == "movie")
        .join(data["title_ratings"], "tconst")
        .filter(col("averageRating") >= 7.5)
        .filter(col("numVotes") >= 10000)
    )
    ua_titles = (
        data["title_akas"]
        .filter(col("region") == "UA")
        .select(col("titleId").alias("ua_titleId"))
        .distinct()
    )
    result = (
        candidate.join(
            ua_titles, candidate["tconst"] == ua_titles["ua_titleId"], "left_anti"
        )
        .select("tconst", "primaryTitle", "startYear", "averageRating", "numVotes")
        .orderBy(desc("averageRating"), desc("numVotes"))
        .limit(200)
    )
    save_result(result, out_dir, "ua_licensing_backlog")


def dubbing_roi_by_language(data: dict, out_dir: str) -> None:
    localized = (
        data["title_akas"]
        .filter(col("language").isNotNull())
        .join(
            data["title_basics"],
            data["title_akas"]["titleId"] == data["title_basics"]["tconst"],
        )
        .filter(col("titleType") == "movie")
        .join(data["title_ratings"], "tconst")
        .filter(col("numVotes") >= 100)
    )
    result = (
        localized.groupBy("language")
        .agg(
            count("tconst").alias("title_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
            spark_round(avg(log10(col("numVotes") + 1)), 2).alias("avg_log_votes"),
        )
        .filter(col("title_count") >= 50)
        .withColumn(
            "dubbing_roi",
            spark_round(col("avg_rating") * col("avg_log_votes"), 2),
        )
        .orderBy(desc("dubbing_roi"))
        .limit(50)
    )
    save_result(result, out_dir, "dubbing_roi_by_language")


def genre_share_per_region(data: dict, out_dir: str) -> None:
    region_genre = (
        data["title_akas"]
        .filter(col("region").isNotNull())
        .join(
            data["title_basics"],
            data["title_akas"]["titleId"] == data["title_basics"]["tconst"],
        )
        .filter(col("titleType") == "movie")
        .filter(col("genres").isNotNull())
        .withColumn("genre", explode(split(col("genres"), ",")))
        .groupBy("region", "genre")
        .agg(count("tconst").alias("title_count"))
    )
    w_total = Window.partitionBy("region")
    w_rank = Window.partitionBy("region").orderBy(desc("title_count"))
    enriched = (
        region_genre.withColumn(
            "region_total", spark_sum("title_count").over(w_total)
        )
        .withColumn(
            "share_pct",
            spark_round(col("title_count") / col("region_total") * 100, 2),
        )
        .withColumn("rank_in_region", rank().over(w_rank))
        .filter(col("region_total") >= 200)
        .filter(col("rank_in_region") <= 3)
    )
    result = (
        enriched.select(
            "region", "rank_in_region", "genre",
            "title_count", "share_pct", "region_total",
        )
        .orderBy("region", "rank_in_region")
    )
    save_result(result, out_dir, "genre_share_per_region")


def underserved_genre_region_cells(data: dict, out_dir: str) -> None:
    base = (
        data["title_akas"]
        .filter(col("region").isNotNull())
        .join(
            data["title_basics"],
            data["title_akas"]["titleId"] == data["title_basics"]["tconst"],
        )
        .filter(col("titleType") == "movie")
        .filter(col("genres").isNotNull())
        .withColumn("genre", explode(split(col("genres"), ",")))
        .select("region", "genre", "tconst")
    )
    w_region = Window.partitionBy("region")
    local = (
        base.groupBy("region", "genre")
        .agg(count("tconst").alias("local_count"))
        .withColumn("region_total", spark_sum("local_count").over(w_region))
        .withColumn(
            "local_share_pct",
            spark_round(col("local_count") / col("region_total") * 100, 2),
        )
        .filter(col("region_total") >= 200)
    )
    global_genre = base.groupBy("genre").agg(count("tconst").alias("global_count"))
    grand_total = global_genre.agg(spark_sum("global_count").alias("g")).collect()[0][
        "g"
    ]
    global_genre = global_genre.withColumn(
        "global_share_pct",
        spark_round(col("global_count") / grand_total * 100, 2),
    )
    result = (
        local.join(global_genre, "genre")
        .withColumn(
            "share_gap",
            spark_round(col("global_share_pct") - col("local_share_pct"), 2),
        )
        .filter(col("share_gap") >= 5)
        .select(
            "region", "genre",
            "local_share_pct", "global_share_pct", "share_gap",
            "local_count", "region_total",
        )
        .orderBy(desc("share_gap"))
        .limit(200)
    )
    save_result(result, out_dir, "underserved_genre_region_cells")


def globally_portable_writers(data: dict, out_dir: str) -> None:
    writers = (
        data["title_crew"]
        .filter(col("writers").isNotNull())
        .withColumn("writer_id", explode(split(col("writers"), ",")))
        .select(col("tconst").alias("w_tconst"), "writer_id")
    )
    region_reach = (
        writers.join(
            data["title_akas"].filter(col("region").isNotNull()),
            writers["w_tconst"] == data["title_akas"]["titleId"],
        )
        .groupBy("writer_id")
        .agg(countDistinct("region").alias("region_count"))
    )
    title_quality = (
        writers.join(
            data["title_ratings"],
            writers["w_tconst"] == data["title_ratings"]["tconst"],
        )
        .groupBy("writer_id")
        .agg(
            countDistinct("w_tconst").alias("title_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
        )
    )
    combined = (
        region_reach.join(title_quality, "writer_id")
        .filter(col("title_count") >= 3)
        .filter(col("region_count") >= 5)
    )
    w = Window.orderBy(desc("region_count"), desc("avg_rating"))
    result = (
        combined.withColumn("rank", row_number().over(w))
        .join(
            data["name_basics"],
            combined["writer_id"] == data["name_basics"]["nconst"],
        )
        .select("rank", "primaryName", "region_count", "title_count", "avg_rating")
        .orderBy("rank")
        .limit(50)
    )
    save_result(result, out_dir, "globally_portable_writers")


def emerging_content_source_countries(data: dict, out_dir: str) -> None:
    originals = (
        data["title_akas"]
        .filter(col("isOriginalTitle") == 1)
        .filter(col("region").isNotNull())
        .select(col("titleId").alias("o_tconst"), "region")
    )
    titles = (
        originals.join(
            data["title_basics"],
            originals["o_tconst"] == data["title_basics"]["tconst"],
        )
        .filter(col("titleType") == "movie")
        .filter(col("startYear").isNotNull())
        .join(
            data["title_ratings"],
            originals["o_tconst"] == data["title_ratings"]["tconst"],
        )
        .filter(col("numVotes") >= 100)
        .select("region", col("startYear").alias("year"), "averageRating")
    )
    bucketed = (
        titles.withColumn(
            "era",
            when(col("year").between(LATEST_FULL_YEAR - 4, LATEST_FULL_YEAR), "recent")
            .when(col("year").between(LATEST_FULL_YEAR - 9, LATEST_FULL_YEAR - 5), "prior"),
        )
        .filter(col("era").isNotNull())
        .groupBy("region", "era")
        .agg(
            count("year").alias("title_count"),
            spark_round(avg("averageRating"), 2).alias("avg_rating"),
        )
    )
    pivoted = (
        bucketed.groupBy("region")
        .pivot("era", ["recent", "prior"])
        .agg(
            spark_max("title_count").alias("count"),
            spark_max("avg_rating").alias("rating"),
        )
        .filter(col("recent_count").isNotNull() & col("prior_count").isNotNull())
        .filter(col("prior_count") >= 30)
        .withColumn(
            "count_growth_pct",
            spark_round(
                (col("recent_count") - col("prior_count")) / col("prior_count") * 100, 1
            ),
        )
    )
    w = Window.orderBy(desc("count_growth_pct"))
    result = (
        pivoted.withColumn("rank", dense_rank().over(w))
        .select(
            "rank", "region",
            "recent_count", "prior_count", "count_growth_pct",
            "recent_rating",
        )
        .orderBy("rank")
        .limit(50)
    )
    save_result(result, out_dir, "emerging_content_source_countries")


def run(data: dict, output_path: str) -> None:
    print("\n=== DISTRIBUTOR QUERIES ===")
    out = f"{output_path}/distributor"
    ua_licensing_backlog(data, out)
    dubbing_roi_by_language(data, out)
    genre_share_per_region(data, out)
    underserved_genre_region_cells(data, out)
    globally_portable_writers(data, out)
    emerging_content_source_countries(data, out)
