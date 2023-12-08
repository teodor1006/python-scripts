import boto3

ACCESS_KEY = "replace with access key"
SECRET_KEY = "replace with secret access key"

def get_ec2_resource():
    return boto3.resource('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def get_unused_volumes():
    return [volume.id for volume in get_ec2_resource().volumes.filter(State='available', Attachments=[])]

def delete_volumes(volume_ids):
    ec2 = get_ec2_resource()
    for volume_id in volume_ids:
        print(f"Deleting volume {volume_id}")
        ec2.Volume(volume_id).delete()

def main():
    ec2_client = boto3.client('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:
        print(f"Checking for unused volumes in region {region}")
        boto3.setup_default_session(region_name=region)
        unused_volumes = get_unused_volumes()
        
        if unused_volumes:
            delete_volumes(unused_volumes)
        else:
            print(f"No unused volumes found in region {region}")

if __name__ == "__main__":
    main()



