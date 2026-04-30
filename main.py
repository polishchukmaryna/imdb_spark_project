from pyspark.sql import SparkSession

from src.extraction import extract_all
from src.preprocessing import preprocess_all
from src.queries import agency, distributor, streaming, studio

DATA_PATH = "/app/data"
OUTPUT_PATH = "/app/output"


def main():
    spark = (
        SparkSession.builder
        .appName("IMDB Analysis")
        .master("local[*]")
        .config("spark.driver.memory", "8g")
        .config("spark.sql.shuffle.partitions", "100")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    raw = extract_all(spark, DATA_PATH)
    clean = preprocess_all(raw)

    studio.run(clean, OUTPUT_PATH)
    distributor.run(clean, OUTPUT_PATH)
    streaming.run(clean, OUTPUT_PATH)
    agency.run(clean, OUTPUT_PATH)

    spark.stop()


if __name__ == "__main__":
    main()
