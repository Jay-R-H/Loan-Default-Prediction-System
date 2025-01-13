from pyspark.sql import functions as F
from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Aggregating average age by housing type:
avg_age_by_housing = df.groupBy("housing").agg(
    F.avg("age").alias("avg_age")
)

# Results:
avg_age_by_housing.show()
