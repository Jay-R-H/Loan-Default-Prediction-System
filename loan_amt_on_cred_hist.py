from pyspark.sql import functions as F
from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Aggregating total loan amount by credit history:
loan_by_credit_history = df.groupBy("credit_history").agg(
    F.sum("amount").alias("total_loan_amount")
)

# Results:
loan_by_credit_history.show()
