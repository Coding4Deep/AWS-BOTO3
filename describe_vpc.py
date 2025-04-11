import boto3
import json


def describe_vpcs():
    ec2 = boto3.client('ec2')

    try:
        response = ec2.describe_vpcs()

        vpcs = response['Vpcs']
        # print(type(vpcs))
        # json_str = json.dumps(vpcs, indent=4)
        # print(json_str)
        print("-----------------------------------------------------")
        # print(vpcs)
        
        if not vpcs:
            print("No VPCs found in this region.")
            return

        for vpc in vpcs:
            vpc_id = vpc['VpcId']
            cidr = vpc['CidrBlock']
            state = vpc['State']

            if vpc['IsDefault'] == True:
                print("its a default VPC")
            else:
                print("its not a default VPC")

            print(f"VPC ID     : {vpc_id}")
            print(f"CIDR Block : {cidr}")
            print(f"State      : {state}")
            print("-" * 40)

    except Exception as e:
        print(f"Error: {e}")

     

if __name__ == '__main__':
    describe_vpcs()
