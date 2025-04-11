import boto3
ec2 = boto3.client('ec2')


def create_vpc():
    
    cidrblock = '10.0.0.0/16' 
    try:
        vpc_response=ec2.create_vpc(
            CidrBlock=cidrblock,
            AmazonProvidedIpv6CidrBlock=False,
            InstanceTenancy='default'
        )

        vpc_id = vpc_response['Vpc']['VpcId']
        print(f"VPC created with ID: {vpc_id}")
        print("-----------------------------------------------------")
        print("VPCs are created successfully")
        print("-----------------------------------------------------")
    except Exception as e:
        print(f"Error: {e}")
        print("-----------------------------------------------------")
        print("VPCs are not created successfully")
        print("-----------------------------------------------------")
# Set the CIDR block for the VPC
create_vpc()



def describe_vpc():
    res=ec2.describe_vpcs()
    count=0
    try:
        if not res['Vpcs']:
            print("No VPCs found in this region.")
            return
        for vpc in res['Vpcs']:
            vpc_id = vpc['VpcId']
            cidr = vpc['CidrBlock']
            state = vpc['State']
            print("-----------------------------------------------------")
            print(f"VPC ID is : {vpc_id}")
            print(f"VPC CIDR is : {cidr}")
            print(f"VPC State is : {state}")
            print("-----------------------------------------------------")
            count+=1
    except Exception as e :
        print(f"Error: {e}")
        print("-----------------------------------------------------")
        print("VPCs are not described successfully")
        print("-----------------------------------------------------") 
    return count  

count=describe_vpc()
print(f"VPC in this region are: {count}")

if count>3:
    print("-----------------------------------------------------")
    def delete_vpc():
        res=ec2.describe_vpcs()
        try:
            for vpc in res['Vpcs']:
                if vpc['IsDefault'] == False:
                    ec2.delete_vpc(VpcId=vpc['VpcId'])
                else:
                    print("its a default VPC and cannot be deleted")
                    print("-----------------------------------------------------")
        except Exception as e:
            print(f"Error: {e}")
    delete_vpc()