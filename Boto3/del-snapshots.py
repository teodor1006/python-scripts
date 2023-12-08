import boto3

AWS_ACCESS_KEY_ID = "replace with access key"
AWS_SECRET_ACCESS_KEY = "replace with secret access key"

def get_ec2_client(region):
    return boto3.client('ec2', region_name=region, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def cleanup_snapshots():
    # Create an EC2 client to get the list of regions
    ec2_client = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    # Get a list of region names
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    # Iterate over each region
    for region in regions:
        print(f"Cleaning up snapshots in {region}")
        
        # Create an EC2 client for the specific region
        ec2_client_region = get_ec2_client(region)
        
        # Get the list of snapshots owned by the account in the current region
        snapshots = ec2_client_region.describe_snapshots(OwnerIds=['self'])['Snapshots']
        
        # Iterate over each snapshot in the region and delete it
        for snapshot in snapshots:
            print(f"Deleting snapshot {snapshot['SnapshotId']}")
            ec2_client_region.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
        
        print(f"Finished cleaning up snapshots in {region}")

if __name__ == '__main__':
    cleanup_snapshots()


