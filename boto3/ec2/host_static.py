import boto3

# ---- USER CONFIG ----
REGION = "ap-south-1"            # Change your AWS region
KEY_PAIR_NAME = "ap-south-key-pair"     # Existing AWS key pair
SECURITY_GROUP_ID = "sg-0ef65acfb315c6c27"  # Must allow 22, 80
GIT_REPO = "https://github.com/kanishk-malhotra/icecream_project.git"

# ---- CONNECT TO EC2 ----
ec2 = boto3.resource('ec2', region_name=REGION)

# ---- USER DATA SCRIPT (runs automatically at boot) ----
USER_DATA = f"""#!/bin/bash
apt update -y
apt install -y nginx git
systemctl enable nginx
systemctl start nginx

# Deploy project
rm -rf /var/www/html/*
git clone {GIT_REPO} /var/www/html

# Permissions
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

# Restart Nginx
systemctl restart nginx
"""

# ---- CREATE EC2 INSTANCE ----
instances = ec2.create_instances(
    ImageId='ami-0f918f7e67a3323f0',  # Ubuntu 22.04 LTS for ap-south-1
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName=KEY_PAIR_NAME,
    SecurityGroupIds=[SECURITY_GROUP_ID],
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'StaticWebsiteServer'}]
    }],
    UserData=USER_DATA
)

instance = instances[0]
print("🚀 Launching EC2 instance... ID:", instance.id)

# ---- WAIT UNTIL RUNNING ----
instance.wait_until_running()
instance.reload()
print("✅ EC2 Instance is running")
print("🌍 Public IP:", instance.public_ip_address)
print(f"👉 Open in browser: http://{instance.public_ip_address}")
