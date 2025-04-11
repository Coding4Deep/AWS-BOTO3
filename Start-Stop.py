import boto3
import json

ec2 = boto3.client('ec2')
ec2_response=ec2.describe_instances()

#print(ec2_response)
##json_string=json.dumps(ec2_response, indent=4, default=str) 
#print(json_string)
print("-----------------------------------------------------")
# Loop through the reservations and instances

for reservation in ec2_response["Reservations"]:
    for instance in reservation["Instances"]:
        Instance_ID=instance["InstanceId"]
        Private_Ip=instance["PrivateIpAddress"]
        print(f"Instance Id is : {Instance_ID}, Private Ip Addrr is : {Private_Ip}")

print("-----------------------------------------------------")
def start_ec2_instance(instance_id):

    try:
        # Start the instance
        print(f"Starting instance: {instance_id}")
        ec2.start_instances(InstanceIds=[instance_id])

        # Wait for it to be in 'running' state
        print("Waiting for instance to enter 'running' state...")
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        print("Instance is now running.")

        # Fetch public IP address using describe_instances
        response = ec2.describe_instances(InstanceIds=[instance_id])                                                          
        instance = response['Reservations'][0]['Instances'][0]
        public_ip = instance.get('PublicIpAddress')

        # Alternatively, you can use the following line to get the public IP
        # directly from the response without checking for 'PublicIpAddress'
        # public_ip = response['Reservations'][0]['Instances'][0].get('PublicIpAddress')

        if public_ip:
            print(f"Public IP Address: {public_ip}")
        else:
            print("Public IP not assigned. Instance may be in a private subnet.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    start_ec2_instance(Instance_ID)


print("-----------------------------------------------------")
print("Stopping Instance")

ec2.stop_instances(InstanceIds=[Instance_ID])

# Optionally wait until stopped
waiter = ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[Instance_ID])

print(f"Instance {Instance_ID} has been stopped.")