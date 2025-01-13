from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to calculate the average loan amount and default rate based on employment duration:
employment_duration_analysis_query = """
SELECT 
    employment_duration,
    AVG(amount) AS avg_loan_amount,
    ROUND(SUM(CASE WHEN default = 'yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS default_rate
FROM loan_data
GROUP BY employment_duration
ORDER BY employment_duration
"""

# Executing the query:
employment_duration_analysis = spark.sql(employment_duration_analysis_query)

# Results:
employment_duration_analysis.show()
