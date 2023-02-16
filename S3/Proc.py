import boto3
from botocore.config import Config

# Set up the proc user's AWS access key ID and secret access key
aws_access_key_id = 'your_proc_user_access_key_id'
aws_secret_access_key = 'your_proc_user_secret_access_key'

# Set up the AWS session with the proc user's credentials and a custom configuration
config = Config(
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    config=config
)

# Create an S3 client using the configured session
s3 = session.client('s3')

# Access the S3 bucket using the S3 client
bucket_name = 'your_s3_bucket_name'
response = s3.list_objects_v2(Bucket=bucket_name)

# Process the response as needed
for obj in response['Contents']:
    print(obj['Key'])
