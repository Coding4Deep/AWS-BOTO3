
import boto3
import os

# Define AWS Region
region = "us-east-1"

# Initialize EC2 client
ec2_client = boto3.client("ec2", region_name=region)

# Key pair name
key_pair_name = "my-new-keypair4"

# Create a new key pair
response = ec2_client.create_key_pair(KeyName=key_pair_name)

#Save the private key to a .pem file
private_key = response["KeyMaterial"]
pem_file_path = f"{key_pair_name}.pem"

with open(pem_file_path, "w") as pem_file:
    pem_file.write(private_key)

# Set correct permissions for the key file (for Linux/macOS)

os.chmod(pem_file_path, 0o400)

print(f"New key pair created: {key_pair_name} (Saved as {pem_file_path})")







# import boto3

# ec2_client = boto3.client('ec2')

# response = ec2_client.create_key_pair(
#     KeyName='my-key-pair',
#     KeyType='rsa',
#     TagSpecifications=[
#         {
#             'ResourceType': 'key-pair',
#             'Tags': [
#                 {'Key': 'Project', 'Value': 'DevOps'},
#                 {'Key': 'Owner', 'Value': 'Admin'}
#             ]
#         }
#     ],
#     KeyFormat='pem',
#     DryRun=False  # Set True to test without creating the key
# )

# print(response)


print("-------------------------------------------------------------------")


def create_key_pairs():
    print("Creating Key Pairs !")
    key_pair_name=sys.argv[1]
    response=ec2.create_key_pairs(KeyName=key_pair_name)
    
    privateKey=response["KeyMaterial"]
    filename=f"{key_pair_name}".pem
    with open("filename","w"):
        filename.write(privateKey)
    os.chmod("filename",0400)
    print(f"New key pair created: {key_pair_name} (Saved as {pem_file_path})")
    
create_key_pairs
print("-------------------------------------------------------------------")