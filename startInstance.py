import boto3
import time

ec2=boto3.client('ec2')
ec2_response=ec2.describe_instances()

for reservation in ec2_response['Reservations']:
    for instance in reservation['Instances']:        
        instance_id = instance["InstanceId"]
        print(f"Instance ID: {instance_id}")
          
# start_instance.py



# Replace this with your EC2 instance ID
INSTANCE_ID = instance_id 

def start_instance(instance_id):
    ec2_resource = boto3.resource('ec2')

    try:
        print(f"Starting EC2 instance: {instance_id}...")
        ec2.start_instances(InstanceIds=[instance_id])

        print("Waiting for instance to reach 'running' state...")
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])

        print("Instance is now running.")

        # Fetch instance info and get public IP
        instance = ec2_resource.Instance(instance_id)
        instance.load()  # Refresh data

        public_ip = instance.public_ip_address
        print(f"Public IP address: {public_ip}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    start_instance(INSTANCE_ID)
