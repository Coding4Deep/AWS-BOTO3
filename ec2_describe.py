import boto3
import orjson
import json

# Create EC2 client
ec2_client = boto3.client("ec2")

# Fetch instance details
response = ec2_client.describe_instances()
#Convert datetime objects to strings using str()
response_str = json.loads(json.dumps(response, default=str))
# Pretty-print the modified response
print(json.dumps(response_str, indent=4))
# print(orjson.dumps(response, option=orjson.OPT_INDENT_2).decode())

print(len(response["Reservations"]))

count=0

#Print all instances (running & stopped)
print("EC2 Instances (including stopped ones):")
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]
        instance_type = instance["InstanceType"]
        private_ip = instance["PrivateIpAddress"]
        public_ip = instance.get("PublicIpAddress", "N/A")
        count+=1
        print(f"ID: {instance_id}, Type: {instance_type}, State: {state}, Public IP: {public_ip}, private IP: {private_ip}  ")


print("No of ec2 instance is :" ,count)