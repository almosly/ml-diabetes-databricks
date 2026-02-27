from pyspark.sql import SparkSession
from ml_diabetes.config.settings import DataConfig


def load_data(spark: SparkSession):
    """
    Load dataset from Unity Catalog using Spark.
    Returns Spark DataFrame.
    """
    config = DataConfig()
    df = spark.table(config.full_table_name)
    return df