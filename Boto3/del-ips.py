import boto3

# Replace with your AWS access key and secret access key
aws_access_key_id = "your_access_key"
aws_secret_access_key = "your_secret_key"

# Create an EC2 resource object
ec2 = boto3.resource("ec2", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

unused_ips = {}

# Iterate through all AWS regions
for region in ec2.meta.client.describe_regions()["Regions"]:
    region_name = region["RegionName"]
    
    try:
        # Create an EC2 client for the current region
        ec2conn = boto3.client("ec2", region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        
        # Get a list of Elastic IPs in VPC
        addresses = ec2conn.describe_addresses(Filters=[{"Name": "domain", "Values": ["vpc"]}])["Addresses"]
        
        # Check and release unused Elastic IPs
        for address in addresses:
            if "AssociationId" not in address and address["AllocationId"] not in unused_ips:
                unused_ips[address["AllocationId"]] = region_name
                ec2conn.release_address(AllocationId=address["AllocationId"])
                print(f"Deleted unused Elastic IP {address['PublicIp']} in region {region_name}")
    except Exception as e:
        print(f"No access to region {region_name}: {e}")

# Display results
print(f"Found and deleted {len(unused_ips)} unused Elastic IPs across all regions:")
print(unused_ips)


