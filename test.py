from pyspark.sql import SparkSession
from pyspark.sql.functions import col, broadcast
import time

# Spark Cluster Simulation
spark = SparkSession.builder \
    .appName("Databricks-Lab-Cluster-Sim") \
    .config("spark.executor.instances", "4") \
    .config("spark.executor.cores", "4") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.default.parallelism", "200") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.sql.adaptive.skewJoin.enabled", "true") \
    .config("spark.sql.autoBroadcastJoinThreshold", "50MB") \
    .config("spark.memory.fraction", "0.6") \
    .config("spark.memory.storageFraction", "0.3") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("\n=== Spark Config Loaded ===")
print("Executors:", spark.conf.get("spark.executor.instances"))
print("Cores:", spark.conf.get("spark.executor.cores"))
print("Shuffle partitions:", spark.conf.get("spark.sql.shuffle.partitions"))
print("AQE enabled:", spark.conf.get("spark.sql.adaptive.enabled"))


# Test Data Generation
print("\nGenerating datasets...")

big_df = spark.range(0, 20_000_000) \
    .withColumn("key", (col("id") % 10_000)) \
    .withColumnRenamed("id", "big_id")

small_df = spark.range(0, 10_000) \
    .withColumnRenamed("id", "key")

# Partitioning
big_df = big_df.repartition(200, "key")
print("Partitions:", big_df.rdd.getNumPartitions())

# Cache test
big_df.cache()
big_df.count()   # materialización


# Join test (Broadcast)
start = time.time()

joined_df = big_df.join(broadcast(small_df), "key")

count = joined_df.count()

end = time.time()


# Metrics

print("\n=== Test Results ===")
print("Rows:", count)
print("Execution time (s):", round(end - start, 2))


# Explain Plan


print("\n=== Physical Plan ===")
joined_df.explain(mode="formatted")
