import boto3

try:
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Describe Subnets
    response = ec2.describe_subnets()
    subnets = response['Subnets']

    # Print Subnet details
    for subnet in subnets:
        print(f"Subnet ID: {subnet['SubnetId']}")

except Exception as e:
    print(f"An error occurred: {e}")


