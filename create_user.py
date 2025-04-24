import boto3
import sys

# Initialize boto3 IAM client
iam = boto3.client('iam')

def create_user():
    # Taking user name input from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    user_name = sys.argv[1]
    
    try:
        # Create the IAM user
        response = iam.create_user(UserName=user_name)
        print(f"User {user_name} created successfully.")
        
        # Optionally, you can also attach a policy or add user to groups
        # For example, attaching the "AdministratorAccess" policy
        iam.attach_user_policy(UserName=user_name, PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess")
        print(f"AdministratorAccess policy attached to {user_name}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_user()
