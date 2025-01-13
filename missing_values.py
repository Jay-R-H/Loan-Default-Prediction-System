from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count

# Initializing Spark session:
spark = SparkSession.builder.appName("BasicInfo").getOrCreate()

# Reading CSV file into DataFrame:
df = spark.read.csv("cleaned_credit.csv", header=True, inferSchema=True)

# Identifying the count of null values for each column:
missing_count = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])

# Count of missing values for each column:
missing_count.show()
