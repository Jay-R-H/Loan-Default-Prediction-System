from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("credit_with_loan_duration_category.csv", header=True, inferSchema=True)

# Registering DataFrame as a SQL temporary view:
df.createOrReplaceTempView("loan_data")

# SQL query to analyze loan amount distribution by credit history:
loan_amount_credit_history_query = """
SELECT 
    credit_history, 
    AVG(amount) as avg_loan_amount,
    MIN(amount) as min_loan_amount,
    MAX(amount) as max_loan_amount
FROM loan_data
GROUP BY credit_history
ORDER BY avg_loan_amount DESC
"""

# Executing the query:
loan_amount_credit_history_analysis = spark.sql(loan_amount_credit_history_query)

# Results:
loan_amount_credit_history_analysis.show()
