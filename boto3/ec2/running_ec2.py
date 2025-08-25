import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Get all running instances
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)

# Count running instances
running_count = 0
for reservation in response['Reservations']:
    running_count += len(reservation['Instances'])

print(f"Number of running instances: {running_count}")



