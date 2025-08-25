import boto3

# Create EC2 client to list all regions
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Get all AWS regions
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    ec2 = boto3.client('ec2', region_name=region)

    # Get all instances (any state)
    response = ec2.describe_instances()

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        print(f"Terminating instances in {region}: {instance_ids}")
        ec2.terminate_instances(InstanceIds=instance_ids)
    else:
        print(f"No instances found in {region}")
