from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to get top purposes based on loan amount:
top_purposes_query = """
SELECT purpose, SUM(amount) as total_amount
FROM loan_data
GROUP BY purpose
ORDER BY total_amount DESC
LIMIT 4
"""

# Executing the query:
top_purposes = spark.sql(top_purposes_query)

# Results:
top_purposes.show()
