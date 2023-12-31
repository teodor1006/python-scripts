import boto3

# Replace it with your actual AWS Region
AWS_REGION = 'your AWS Region'

def get_latest_two_images_tags(repo_name, client):
    response = client.describe_images(repositoryName=repo_name)
    images = response['imageDetails']

    # Sort the list of images by creation date
    sorted_images = sorted(images, key=lambda x: x['imagePushedAt'],reverse=True)

    # Get the last 2 images
    latest_two_images = sorted_images[:2]

    # Retrieve image tags
    image_tags = [img['imageTags'][0] for img in latest_two_images]
    return image_tags

ecr_client = boto3.client('ecr', region_name=AWS_REGION)
# Replace it with your actual repo name
repository_name = "your repository name"   
latest_image_tags = get_latest_two_images_tags(repository_name,ecr_client)

print(f"Latest image tags for {repository_name} in {AWS_REGION}: {latest_image_tags}")