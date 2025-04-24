import boto3
import sys
import os

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

def describe_instances():
    #This function retrieves and prints the public and private IP addresses of all EC2 instances.
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            Instance_ID = instance["InstanceId"]
            Public_IP = instance.get("PublicIpAddress", "N/A")
            Private_IP = instance["PrivateIpAddress"]
            print(f"IP Addresses of Instance {Instance_ID} are: {Public_IP} and {Private_IP}")

describe_instances()
print("-------------------------------------------------------------------")



def describe_keypairs():
    try:
        response = ec2.describe_key_pairs()
        keyName=[]
        
        for i, keys in enumerate(response["KeyPairs"], start=1):
            key_name = keys["KeyName"]		
            print(f"Key pair {i}: {key_name}")
            keyName.append(key_name)
        return keyName
    except Exception as e:
        print(f"Error! {e}")
    
keyName=describe_keypairs()    
print("-------------------------------------------------------------------")


def delete_keypairs():
    try:
        if keyName!="devops":
            print("Deleting key pairs...")
            for key in keyName:
                print(f"Deleting key pair: {key}")
                ec2.delete_key_pair(KeyName=key)
                print(f"Key pair {key} deleted successfully.")
        else:   
            print("Key pair devops cannot be deleted.")
    except Exception as e:
        print(f"Error! {e}")
delete_keypairs()
print("-------------------------------------------------------------------")


def create_key_pairs():

    try:
        print("Creating new key pair...")
        key_pair_name=sys.argv[1]
        response=ec2.create_key_pair(KeyName=key_pair_name)
        
        privateKey=response["KeyMaterial"]
        filename = os.path.expanduser(f"~/{key_pair_name}.pem")
        with open(filename,"w") as file:
            file.write(privateKey)
        os.chmod(filename, 0o400)
        print("still Creating new key pair...")
        print(f"New key pair created: {key_pair_name} (Saved as {filename})")
    except Exception as e:
        print(f"Error! {e}")
        
create_key_pairs()
print("-------------------------------------------------------------------")



def describe_vpc():
    try:
        i=1
        response = ec2.describe_vpcs()
        for vpc in response["Vpcs"]:
            vpc_id = vpc["VpcId"]
            cidr_block = vpc["CidrBlock"]
            print(f"VPC {i}: ID: {vpc_id}, CIDR Block: {cidr_block}, is it a default VPC? : {vpc['IsDefault']}")
            i+=1
    except Exception as e:
        print(f"Error! {e}")
    return i-1

start=describe_vpc()
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")

def delete_vpc():
    print("Deleting VPCs...") 
    try:
        res=ec2.describe_vpcs()

        for vpc in res["Vpcs"]:
            if vpc["IsDefault"]== False:
                print(f"Deleting VPC: {vpc['VpcId']}")
                ec2.delete_vpc(VpcId=vpc["VpcId"])
                print(f"VPC {vpc['VpcId']} deleted successfully.")
            else:
                print("Default VPC cannot be deleted.")
    except Exception as e:
        print(f"Error! {e}")
delete_vpc()
print("-------------------------------------------------------------------")


def create_vpc():
    try:
        if start<5:
            print("Creating VPC")
            res=ec2.create_vpc(
               CidrBlock="10.10.0.0/25",
               AmazonProvidedIpv6CidrBlock=False,
               InstanceTenancy='default'
            )
            VPC_ID=res["Vpc"]["VpcId"]
            print(f"VPC is CreaTed with id : {VPC_ID}")
        else:
            print("VPC number has been reached to the limit")
        print("-----------------------------------------------------")
    except Exception as e:
        print(f"Error! {e}")
    
create_vpc()




def start_stop_ec2():
    try:
        res = ec2.describe_instances()
        for reservation in res["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                state = instance["State"]["Name"]

                if state == "stopped":
                    print(f"Starting instance: {instance_id}")
                    ec2.start_instances(InstanceIds=[instance_id])
                    waiter = ec2.get_waiter("instance_running")
                    waiter.wait(InstanceIds=[instance_id])
                    print(f"EC2 instance {instance_id} started successfully.")
 
                    # Refresh instance details to get updated IPs
                    updated_instance = ec2.describe_instances(InstanceIds=[instance_id])["Reservations"][0]["Instances"][0]
                    Public_IP = updated_instance.get("PublicIpAddress", "N/A")
                    Private_IP = updated_instance["PrivateIpAddress"]
                    print(f"IP Addresses of Instance {instance_id}: Public: {Public_IP}, Private: {Private_IP}")
                else:
                    print(f"Stopping instance: {instance_id}")
                    ec2.stop_instances(InstanceIds=[instance_id])
                    waiter = ec2.get_waiter("instance_stopped")
                    waiter.wait(InstanceIds=[instance_id])
                    print(f"EC2 instance {instance_id} stopped successfully.")

    except Exception as e:
        print(f"Error! {e}")

start_stop_ec2()
print("-------------------------------------------------------------------")