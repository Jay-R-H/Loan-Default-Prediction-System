from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to calculate percentage of loans for each purpose:
loan_purpose_percentage_query = """
SELECT 
    purpose,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loan_data), 2) AS loan_percentage
FROM loan_data
GROUP BY purpose
ORDER BY loan_percentage DESC
"""

# Executing the query:
loan_purpose_percentage_analysis = spark.sql(loan_purpose_percentage_query)

# Results:
loan_purpose_percentage_analysis.show()
