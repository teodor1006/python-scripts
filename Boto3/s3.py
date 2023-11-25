# pip install awscli boto3
import boto3

s3_bucket_name = 'test-boto345' # Make sure to give it a unique name otherwise it won't work
region = 'us-east-1'

def create_s3_bucket():
    s3_client = boto3.client('s3', region_name=region)

    s3_client.create_bucket(Bucket=s3_bucket_name)
    print(f"S3 bucket {s3_bucket_name} created")

#create_s3_bucket()

def delete_s3_bucket():
    s3_client = boto3.client('s3', region_name=region)

    # Delete all objects in the bucket before deleting the bucket
    response = s3_client.list_objects(Bucket=s3_bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_client.delete_object(Bucket=s3_bucket_name, Key=obj['Key'])

    # Delete the bucket
    s3_client.delete_bucket(Bucket=s3_bucket_name)
    print(f"S3 bucket {s3_bucket_name} deleted.")

#delete_s3_bucket()