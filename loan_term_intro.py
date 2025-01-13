from pyspark.sql import SparkSession
from pyspark.sql.functions import when
import pandas as pd

# Initializing Spark session:
spark = SparkSession.builder.appName("Loan Duration Category").getOrCreate()

# Loading dataset:
df = spark.read.csv("cleaned_credit.csv", header=True, inferSchema=True)

# Creating Loan Duration Category column:
df = df.withColumn(
    "loan_duration_category",
    when(df["months_loan_duration"] <= 12, "Short-Term")
    .when((df["months_loan_duration"] > 12) & (df["months_loan_duration"] <= 36), "Medium-Term")
    .otherwise("Long-Term")
)
new_df = df.toPandas()

# Updated dataframe to a new CSV:
new_df.to_csv('credit_with_loan_duration_category.csv', index=False)

spark.stop()
