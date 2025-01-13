from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Reading CSV file into DataFrame:
df = spark.read.csv("credit.csv", header=True, inferSchema=True)

# Displaying the first 5 rows:
df.show(5)
