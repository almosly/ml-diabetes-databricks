from pyspark.sql import SparkSession
from ml_diabetes.data.loader import load_data


def run_training():
    spark = SparkSession.builder.getOrCreate()

    print("Loading data from Unity Catalog...")
    df = load_data(spark)

    print("Data loaded successfully.")
    print(f"Number of rows: {df.count()}")
    print(f"Number of columns: {len(df.columns)}")

    spark.stop()