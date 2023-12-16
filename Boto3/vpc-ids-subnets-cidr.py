import boto3

def get_ec2_client():
    return boto3.client('ec2')

def list_subnets(vpc_id):
    try:
        ec2 = get_ec2_client()
        response = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        subnets = response['Subnets']

        for subnet in subnets:
            print(f"  Subnet ID: {subnet['SubnetId']}, CIDR Block: {subnet['CidrBlock']}")

    except Exception as e:
        print(f"An error occurred while listing subnets: {e}")

def list_security_groups(vpc_id):
    try:
        ec2 = get_ec2_client()
        response = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        security_groups = response['SecurityGroups']

        for sg in security_groups:
            print(f"  Security Group ID: {sg['GroupId']}, Group Name: {sg['GroupName']}")

    except Exception as e:
        print(f"An error occurred while listing security groups: {e}")

def list_vpcs():
    try:
        ec2 = get_ec2_client()
        response = ec2.describe_vpcs()
        vpcs = response['Vpcs']

        for vpc in vpcs:
            print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}")
            list_subnets(vpc['VpcId'])
            list_security_groups(vpc['VpcId'])

    except Exception as e:
        print(f"An error occurred while listing VPCs: {e}")

if __name__ == '__main__':
    list_vpcs()


