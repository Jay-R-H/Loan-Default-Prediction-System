from pyspark.sql import functions as F
from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Aggregating total number of loans by employment duration:
total_loans_by_employment = df.groupBy("employment_duration").agg(
    F.count("months_loan_duration").alias("total_loans")
)

# Results:
total_loans_by_employment.show()
