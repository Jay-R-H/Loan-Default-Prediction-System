import boto3

# Initializing the session:
session = boto3.Session(
    aws_access_key_id='#',
    aws_secret_access_key='#',
    region_name='us-east-2'
)
s3 = session.resource('s3')

# S3 bucket name and the file name:
bucket_name = 'bda-processed-data-bucket'
file_name = 'credit_with_loan_duration_category.csv'
local_file_path = 'credit_with_loan_duration_category.csv'

# The S3 object:
s3_object = s3.Object(bucket_name, file_name)

# Upload the file to S3:
s3_object.upload_file(local_file_path)

print("File uploaded successfully!")
