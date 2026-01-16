'''
Uses Spark
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

def create_spark_session():
    return SparkSession.builder \
        .appName("XometryDemandETL") \
        .config("spark.sql.shuffle.partitions", "8") \
        .getOrCreate()

def load_raw_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def clean_orders(df):
    return (
        df
        .withColumn("order_date", to_date(col("order_date")))
        .filter(col("price") > 0)
        .filter(col("quantity") > 0)
    )

def aggregate_demand(df):
    return (
        df
        .groupBy("order_date", "part_category", "region")
        .sum("quantity")
        .withColumnRenamed("sum(quantity)", "daily_demand")
    )

if __name__ == "__main__":
    spark = create_spark_session()
    raw = load_raw_data(spark, "data/raw/orders.csv")
    clean = clean_orders(raw)
    agg = aggregate_demand(clean)
    agg.write.mode("overwrite").parquet("data/processed/daily_demand")
