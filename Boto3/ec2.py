# pip install awscli boto3
import boto3

def create_ec2():
    ec2_name = 'test'
    instance_type = 't2.micro'
    key_name = 'test-key'  # Create your key_name in advance 
    region = 'us-east-1'
    ami_id = 'ami-0fc5d935ebf8bc3bc' # AMI for Ubuntu22.04

    ec2_client = boto3.client('ec2', region_name=region)

    response = ec2_client.run_instances(
        ImageId=ami_id,  
        InstanceType=instance_type,
        KeyName=key_name,
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': ec2_name},
                ],
            },
        ],
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance {ec2_name} created with ID: {instance_id}")

#create_ec2()

def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} terminated.")

#terminate_instance(instance_id='i-0c5b4ee39bfb7209d')      


