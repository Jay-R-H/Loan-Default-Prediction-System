from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean

# Initialize Spark session
spark = SparkSession.builder.appName("Handle Missing Values").getOrCreate()

# Load dataset
df = spark.read.csv("credit.csv", header=True, inferSchema=True)

# Handle missing values for numerical columns
numerical_columns = [col_name for col_name, dtype in df.dtypes if dtype in ('int', 'double')]
for col_name in numerical_columns:
    mean_value = df.select(mean(col(col_name))).collect()[0][0]
    df = df.fillna({col_name: mean_value})

# Handle missing values for categorical columns
categorical_columns = [col_name for col_name, dtype in df.dtypes if dtype == 'string']
for col_name in categorical_columns:
    mode_value = df.groupBy(col_name).count().orderBy('count', ascending=False).first()[0]
    df = df.fillna({col_name: mode_value})

# Save cleaned DataFrame to CSV
df.write.csv('cleaned_credit.csv', header=True, mode='overwrite')

spark.stop()
