import boto3

session = boto3.Session(
    aws_access_key_id='#',
    aws_secret_access_key='#',
    region_name='us-east-2'
)
s3 = session.resource('s3')

# S3 bucket name and the CSV file name:
bucket_name = 'bda-raw-data-bucket'
file_name = 'credit.csv'
local_file_path = 'cleaned_credit.csv'

# The S3 object:
s3_object = s3.Object(bucket_name, file_name)

# Download the file to local storage:
s3_object.download_file(local_file_path)

print("File downloaded successfully!")
