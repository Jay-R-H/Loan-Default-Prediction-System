from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("BasicInfo").getOrCreate()

# Reading CSV file into DataFrame:
df = spark.read.csv("credit.csv", header=True, inferSchema=True)

# Schema and summary:
df.printSchema()
df.describe().show()
