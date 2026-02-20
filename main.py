import os
from pathlib import Path
from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()

spark = SparkSession.builder \
    .appName("IMDB Ratings Analysis") \
    .master("local[*]") \
    .getOrCreate()

dataset_path = os.getenv('DATASET_PATH', '.')
dataset_file = Path(dataset_path) / 'title.ratings.tsv'

print(f"\nLoading data from {dataset_file}...")
df = spark.read.csv(
    str(dataset_file),
    sep="\t",
    header=True,
    inferSchema=True
)

print("\nFirst 10 rows of the dataset:")
df.show(10)

print("\nData schema:")
df.printSchema()

print("\nTotal number of records:", df.count())

spark.stop()
