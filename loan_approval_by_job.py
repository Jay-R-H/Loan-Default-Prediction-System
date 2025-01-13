from pyspark.sql import functions as F
from pyspark.sql import SparkSession

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Calculating loan approval rate by job type:
loan_approval_by_job = df.groupBy("job").agg(
    F.avg((df["default"] == "yes").cast("int")).alias("approval_rate")
)

# Results:
loan_approval_by_job.show()

