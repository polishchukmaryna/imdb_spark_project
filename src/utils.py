from pyspark.sql import DataFrame


def save_result(df: DataFrame, output_path: str, name: str) -> None:
    print(f"\n>>> Query: {name}")
    print("Execution plan:")
    df.explain(mode="formatted")
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(
        f"{output_path}/{name}"
    )
    print(f"Saved to {output_path}/{name}")