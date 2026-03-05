from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, FloatType
)


NAME_BASICS_SCHEMA = StructType([
    StructField("nconst", StringType(), True),
    StructField("primaryName", StringType(), True),
    StructField("birthYear", IntegerType(), True),
    StructField("deathYear", IntegerType(), True),
    StructField("primaryProfession", StringType(), True),
    StructField("knownForTitles", StringType(), True),
])

TITLE_AKAS_SCHEMA = StructType([
    StructField("titleId", StringType(), True),
    StructField("ordering", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("region", StringType(), True),
    StructField("language", StringType(), True),
    StructField("types", StringType(), True),
    StructField("attributes", StringType(), True),
    StructField("isOriginalTitle", IntegerType(), True),
])

TITLE_BASICS_SCHEMA = StructType([
    StructField("tconst", StringType(), True),
    StructField("titleType", StringType(), True),
    StructField("primaryTitle", StringType(), True),
    StructField("originalTitle", StringType(), True),
    StructField("isAdult", IntegerType(), True),
    StructField("startYear", IntegerType(), True),
    StructField("endYear", IntegerType(), True),
    StructField("runtimeMinutes", IntegerType(), True),
    StructField("genres", StringType(), True),
])

TITLE_CREW_SCHEMA = StructType([
    StructField("tconst", StringType(), True),
    StructField("directors", StringType(), True),
    StructField("writers", StringType(), True),
])

TITLE_EPISODE_SCHEMA = StructType([
    StructField("tconst", StringType(), True),
    StructField("parentTconst", StringType(), True),
    StructField("seasonNumber", IntegerType(), True),
    StructField("episodeNumber", IntegerType(), True),
])

TITLE_PRINCIPALS_SCHEMA = StructType([
    StructField("tconst", StringType(), True),
    StructField("ordering", IntegerType(), True),
    StructField("nconst", StringType(), True),
    StructField("category", StringType(), True),
    StructField("job", StringType(), True),
    StructField("characters", StringType(), True),
])

TITLE_RATINGS_SCHEMA = StructType([
    StructField("tconst", StringType(), True),
    StructField("averageRating", FloatType(), True),
    StructField("numVotes", IntegerType(), True),
])


def _read_tsv(spark: SparkSession, path: str, schema: StructType) -> DataFrame:
    return (
        spark.read
        .option("sep", "\t")
        .option("header", True)
        .option("nullValue", "\\N")
        .schema(schema)
        .csv(path)
    )


def extract_all(spark: SparkSession, data_path: str) -> dict:
    datasets = {
        "name_basics": _read_tsv(spark, f"{data_path}/name.basics.tsv", NAME_BASICS_SCHEMA),
        "title_akas": _read_tsv(spark, f"{data_path}/title.akas.tsv", TITLE_AKAS_SCHEMA),
        "title_basics": _read_tsv(spark, f"{data_path}/title.basics.tsv", TITLE_BASICS_SCHEMA),
        "title_crew": _read_tsv(spark, f"{data_path}/title.crew.tsv", TITLE_CREW_SCHEMA),
        "title_episode": _read_tsv(spark, f"{data_path}/title.episode.tsv", TITLE_EPISODE_SCHEMA),
        "title_principals": _read_tsv(spark, f"{data_path}/title.principals.tsv", TITLE_PRINCIPALS_SCHEMA),
        "title_ratings": _read_tsv(spark, f"{data_path}/title.ratings.tsv", TITLE_RATINGS_SCHEMA),
    }

    for name, df in datasets.items():
        print(f"  {name}: {len(df.columns)} columns")
        df.printSchema()

    return datasets
