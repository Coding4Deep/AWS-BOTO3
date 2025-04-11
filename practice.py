import boto3
import json
import os

ec2_client=boto3.client("ec2")

dir_res=ec2_client.describe_instances()   #give dir res

# print(res)
# json_str=json.dumps(dir_res,default=str)
# json_dir=json.loads(json_str)
# print("dir format is :",json_dir)
# print("-"*250)
# json_data=json.dumps(json_dir,indent=4)
# print(json_data)


for reservation in dir_res["Reservations"]:
    for instance in reservation["Instances"]:
        Instance_ID=instance["InstanceId"]
        print("Instance_ID is : " , Instance_ID)




# Fetch all key pairs
response = ec2_client.describe_key_pairs()

# Print key pair names
for key in response["KeyPairs"]:
    print(f"Key Pair Name: {key['KeyName']}")

# CREATING A KEY PAIR

key_pair_name="test_key4"

response = ec2_client.create_key_pair(KeyName=key_pair_name)
#print(response)
private_key=response["KeyMaterial"]
key_pair_path=f"{key_pair_name}.pem"

with open(key_pair_path,"w") as pemfile:
    pemfile.write(private_key)


print(f"my pem file is with name {key_pair_path} at locatiohn {os.getcwd}")


        
