import os
import subprocess
import boto3

# Set up AWS credentials and region
os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_access_key'
os.environ['AWS_DEFAULT_REGION'] = 'your_aws_region'

# Set up local directory and S3 bucket name
local_dir = '/path/to/local/directory'
bucket_name = 'your_s3_bucket_name'

# Create S3 client
s3 = boto3.client('s3')

# Get list of files in local directory
files = os.listdir(local_dir)

# Loop through files and upload to S3 bucket
for file in files:
    local_file_path = os.path.join(local_dir, file)
    s3_file_key = file
    subprocess.call(['aws', 's3', 'cp', local_file_path, f's3://{bucket_name}/{s3_file_key}'])
