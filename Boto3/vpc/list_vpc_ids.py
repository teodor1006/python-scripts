import boto3

try:
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Describe VPCs
    response = ec2.describe_vpcs()
    vpcs = response['Vpcs']

    # Print VPC IDs
    for vpc in vpcs:
        print(vpc['VpcId'])

except Exception as e:
    print(f"An error occurred: {e}")
