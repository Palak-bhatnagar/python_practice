import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-020cba7c55df1f615',  # Amazon Linux 2 AMI (update as per your region)
    InstanceType='t3.micro',
    KeyName='palak_ec2_key',           # Replace with your EC2 key pair name
    MinCount=1,
    MaxCount=1,
    # SecurityGroupIds=['sg-0abcd1234efgh5678'],  # Replace with your Security Group ID
    # SubnetId='subnet-0abcd1234efgh5678',       # Replace with your Subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyBoto3Instance'}
            ]
        }
    ]
)

print("Created instance with ID:", response['Instances'][0]['InstanceId'])
