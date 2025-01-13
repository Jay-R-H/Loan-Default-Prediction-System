from pyspark.sql import functions as F
from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Aggregating average loan amount by loan duration category:
avg_loan_by_duration = df.groupBy("loan_duration_category").agg(
    F.avg("amount").alias("avg_loan_amount")
)

# Results:
avg_loan_by_duration.show()
