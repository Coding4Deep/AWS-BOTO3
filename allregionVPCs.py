import boto3

def get_all_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions(AllRegions=False)
    return [region['RegionName'] for region in response['Regions']]

def check_default_vpc_in_all_regions():
    regions = get_all_regions()
    
    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        try:
            response = ec2.describe_vpcs()
            default_vpcs = [vpc for vpc in response['Vpcs'] if vpc['IsDefault']]
            
            print(f"Region: {region}")
            if default_vpcs:
                for vpc in default_vpcs:
                    print(f"✅ Default VPC ID: {vpc['VpcId']}\n")
            else:
                print("❌ No default VPC in this region\n")
        
        except Exception as e:
            print(f"⚠️ Error checking region {region}: {e}\n")

if __name__ == '__main__':
    check_default_vpc_in_all_regions()
