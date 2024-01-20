import boto3

# Create an EC2 resource
ec2 = boto3.resource("ec2")

# Retrieve all key pairs
all_key_pairs = ec2.key_pairs.all()

# Get the names of key pairs used by instances
used_keys = set([instance.key_name for instance in ec2.instances.all()])

# Identify unused key pairs
unused_keys = [key_pair.name for key_pair in all_key_pairs if key_pair.name not in used_keys]

# Delete unused key pairs
for key_name in unused_keys:
    ec2.KeyPair(key_name).delete()

# Print the number of deleted unused key pairs
print(f"Deleted {len(unused_keys)} unused key pairs.")
   