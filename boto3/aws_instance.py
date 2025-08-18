import boto3

# Create EC2 client for initial region to list all regions
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Get all AWS regions
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

total_running = 0
total_non_running = 0

for region in regions:
    ec2 = boto3.client('ec2', region_name=region)

    # Get all instances regardless of state
    response = ec2.describe_instances()

    running_count = 0
    non_running_count = 0

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']  # e.g., running, stopped, terminated
            name_tag = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), "No Name")

            print(f"Region: {region} | Instance ID: {instance_id} | Name: {name_tag} | State: {state}")

            if state == 'running':
                running_count += 1
            else:
                non_running_count += 1

    if running_count > 0 or non_running_count > 0:
        print(f"Summary for {region} → Running: {running_count} | Not Running: {non_running_count}\n")

    total_running += running_count
    total_non_running += non_running_count

print(f"Total Running Instances: {total_running}")
print(f"Total Not Running Instances: {total_non_running}")

