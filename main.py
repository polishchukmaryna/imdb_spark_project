from pyspark.sql import SparkSession

from src.extraction import extract_all
from src.preprocessing import preprocess_all

DATA_PATH = "/app/data"
OUTPUT_PATH = "/app/output"


def main():
    spark = (
        SparkSession.builder
        .appName("IMDB Analysis")
        .master("local[*]")
        .config("spark.driver.memory", "4g")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    raw = extract_all(spark, DATA_PATH)
    clean = preprocess_all(raw)

    spark.stop()


if __name__ == "__main__":
    main()
