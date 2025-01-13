from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to analyze loan duration vs. age:
loan_duration_age_query = """
SELECT 
    loan_duration_category, 
    AVG(age) as average_age
FROM loan_data
GROUP BY loan_duration_category
ORDER BY average_age
"""

# Executing the query:
loan_duration_age_analysis = spark.sql(loan_duration_age_query)

# Results:
loan_duration_age_analysis.show()

# SQL query to analyze loan duration vs. age with min and max age:
loan_duration_age_min_max_query = """
SELECT 
    loan_duration_category, 
    MIN(age) as min_age,
    MAX(age) as max_age
FROM loan_data
GROUP BY loan_duration_category
ORDER BY loan_duration_category
"""

# Execute the query
loan_duration_age_min_max_analysis = spark.sql(loan_duration_age_min_max_query)

# Show the results
loan_duration_age_min_max_analysis.show()
