# pip install awscli boto3
import boto3

region = 'us-east-1'
ecr_repo_name = 'test-boto3-repo'

def create_ecr_repository():
    ecr_client = boto3.client('ecr', region_name=region)

    response = ecr_client.create_repository(repositoryName=ecr_repo_name)
    ecr_repo_uri = response['repository']['repositoryUri']
    print(f"ECR repository {ecr_repo_name} created with URI: {ecr_repo_uri}")

#create_ecr_repository()

def delete_ecr_repository():
    ecr_client = boto3.client('ecr', region_name=region)

    # List images in the repository
    images = ecr_client.list_images(repositoryName=ecr_repo_name)['imageIds']
    if images:
        # Batch delete images
        ecr_client.batch_delete_image(repositoryName=ecr_repo_name, imageIds=images)

    ecr_client.delete_repository(repositoryName=ecr_repo_name, force=True)
    print(f"ECR repository {ecr_repo_name} deleted.")

#delete_ecr_repository()