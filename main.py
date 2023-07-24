import boto3

def create_ec2_instance(image_id, instance_type, key_name, security_group_id, subnet_id):
    # Create a Boto3 EC2 client
    ec2 = boto3.client('ec2')

    # Launch the EC2 instance
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[security_group_id],
        SubnetId=subnet_id
    )

    instance_id = response['Instances'][0]['InstanceId']

    return instance_id

if __name__ == "__main__":
    # Replace these values with your actual configuration
    IMAGE_ID = "ami-xxxxxxxxxxxxxxxxx"  # Amazon Linux 2 AMI ID or any other suitable AMI
    INSTANCE_TYPE = "t2.micro"  # You can choose any instance type
    KEY_NAME = "your_key_pair_name"  # Replace with your key pair name
    SECURITY_GROUP_ID = "sg-xxxxxxxxxxxxxxxxx"  # Replace with your security group ID
    SUBNET_ID = "subnet-xxxxxxxxxxxxxxxxx"  # Replace with your subnet ID

    instance_id = create_ec2_instance(IMAGE_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_ID, SUBNET_ID)
    print(f"EC2 instance created with ID: {instance_id}")
