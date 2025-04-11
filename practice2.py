import boto3
import sys

ec2_client=boto3.client("ec2")
ec2_resposnse=ec2_client.describe_instances()

#describe or list ec2

for reservation in  ec2_resposnse["Reservations"]:
    for instance in reservation["Instances"]:
        Instance_Id=instance["InstanceId"]
        Private_IP_Address=instance["PrivateIpAddress"]
        Publice_Ip=instance.get("PublicIpAddress","N/A")
        print(Instance_Id,Private_IP_Address,Publice_Ip)
 

#Describe and Create Pem File

key_response=ec2_client.describe_key_pairs()
#print(key_response)
for key in key_response["KeyPairs"]:
    print(f"name of key pair is : {key['KeyName']}")

key_name=sys.argv[1]



def key_exist():
    try:
        for key in key_response["KeyPairs"]:
            if key['KeyName']==key_name:
                return True
    except Exception as e:
        print(f"getting some error ! {e}")
    return False      

try:
    if key_exist():
        print("key with this name exist try another name !")
    else:
        key_create=ec2_client.create_key_pair(KeyName=key_name)
        # print(key_create)
        privatekey=key_create['KeyMaterial']
        myfile=f"{key_name}.pem"
        with open(myfile,'w') as pemfile:
            pemfile.write(privatekey)
            print(f"pem file created with name {key_name}.pem")
            print(f"pem file created with name {key_name}.pem")
except Exception as e:
    print(f"error {e}")
        
       



