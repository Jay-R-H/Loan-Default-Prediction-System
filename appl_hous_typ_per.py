from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to calculate percentage of people with different housing types:
housing_percentage_query = """
SELECT 
    housing,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loan_data), 2) AS housing_percentage
FROM loan_data
GROUP BY housing
"""

# Executing the query:
housing_percentage_analysis = spark.sql(housing_percentage_query)

# Results:
housing_percentage_analysis.show()
