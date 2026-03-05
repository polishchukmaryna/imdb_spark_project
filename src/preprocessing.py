from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, when


def _null_counts(df: DataFrame) -> None:
    print("  Null counts per column:")
    null_expr = [
        count(when(col(c).isNull(), c)).alias(c) for c in df.columns
    ]
    df.select(null_expr).show(vertical=True)


def _print_stats(name: str, df: DataFrame) -> None:
    print(f"\n--- {name} ---")
    row_count = df.count()
    print(f"  Row count: {row_count}")
    df.printSchema()
    _null_counts(df)

    numeric_cols = [
        f.name for f in df.schema.fields
        if str(f.dataType) in ("IntegerType()", "FloatType()", "DoubleType()")
    ]
    if numeric_cols:
        print(f"  Numeric feature statistics ({', '.join(numeric_cols)}):")
        df.select(numeric_cols).describe().show()


def _clean_title_basics(df: DataFrame) -> DataFrame:
    df = df.drop("isAdult")
    df = df.dropna(subset=["tconst", "primaryTitle"])
    df = df.dropDuplicates(["tconst"])
    return df


_CLEANERS = {
    "title_basics": _clean_title_basics,
    # TODO implement the rest of cleaners
}


def preprocess_all(raw: dict) -> dict:
    print("\nStart preprocessing...")
    clean = {}
    for name, df in raw.items():
        cleaner = _CLEANERS.get(name)
        if cleaner:
            print(f"\n   {name} BEFORE cleaning")
            _print_stats(name, df)
            df = cleaner(df)
            print(f"\n    {name} AFTER cleaning")
        _print_stats(name, df)
        clean[name] = df
    print("\nFinish preprocessing.")
    return clean
