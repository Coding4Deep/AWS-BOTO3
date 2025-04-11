import boto3 
# import os


ec2_client=boto3.client("ec2")

# response=ec2_client.describe_instances()

# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         Instance_Id=instance["InstanceId"]
#         Private_IP=instance["PrivateIpAddress"]
#         Public_Ip=instance.get("PublicIpAddress", "N/A")
#         print("----------------------------------------------------")
#         print(f"Instance Id :{Instance_Id} \nPublic Ip : {Public_Ip}, \nPrivate Ip : {Private_IP}")
#         print("----------------------------------------------------")

key_response=ec2_client.describe_key_pairs()
i=1
for keypair in key_response["KeyPairs"]:
    key_pair=keypair["KeyName"]
    print("----------------------------------------------------")
    print(f"Key Pair {i} : {key_pair}")
    i+=1




Key_pair_Name="prod_key"

def key_pair_exist():
    try:
        key_response=ec2_client.describe_key_pairs()
        for keypair in key_response["KeyPairs"]:
            if keypair["KeyName"]=="key_pair_Name":
                return True
    except Exception as e:
        print(f"getting some error ! {e}")    
    return False

try:
    if  key_pair_exist():
        print("Key Pair with this name exist ! try another ")
    else:
        key_create=ec2_client.create_key_pair(KeyName=Key_pair_Name)
        
        private_key=key_create["KeyMaterial"]
        myfile=f"{Key_pair_Name}.pem"
        
        with open("myfile","w") as file:
             file.write(private_key)
             print(f"your private key is created successfully ! with name : {Key_pair_Name}")
except Exception as e:
    print(f"getting some error ! {e}")

