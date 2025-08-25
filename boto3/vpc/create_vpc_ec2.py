import boto3

# -------- CONFIG --------
REGION = "us-east-1"   # Change region
AMI_ID = "ami-0360c520857e3138f"  # Ubuntu 22.04 LTS in us-east-1
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "vpc-ec2-mykey"  # must exist already
GIT_REPO = "https://github.com/kanishk-malhotra/icecream_project.git"  # <-- put a real repo here

VPC_CIDR = "10.0.0.0/16"
PUBLIC_SUBNET_CIDR = "10.0.1.0/24"
PRIVATE_SUBNET_CIDR = "10.0.2.0/24"

ec2 = boto3.client("ec2", region_name=REGION)


def create_vpc():
    vpc = ec2.create_vpc(CidrBlock=VPC_CIDR)
    vpc_id = vpc["Vpc"]["VpcId"]
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={"Value": True})
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={"Value": True})
    print(f"✅ Created VPC: {vpc_id}")
    return vpc_id


def create_subnets(vpc_id):
    pub_subnet = ec2.create_subnet(
        VpcId=vpc_id, CidrBlock=PUBLIC_SUBNET_CIDR, AvailabilityZone=f"{REGION}a"
    )["Subnet"]["SubnetId"]

    priv_subnet = ec2.create_subnet(
        VpcId=vpc_id, CidrBlock=PRIVATE_SUBNET_CIDR, AvailabilityZone=f"{REGION}b"
    )["Subnet"]["SubnetId"]

    print(f"✅ Public Subnet: {pub_subnet}")
    print(f"✅ Private Subnet: {priv_subnet}")
    return pub_subnet, priv_subnet


def create_igw_and_route(vpc_id, pub_subnet):
    igw_id = ec2.create_internet_gateway()["InternetGateway"]["InternetGatewayId"]
    ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)

    rtb_id = ec2.create_route_table(VpcId=vpc_id)["RouteTable"]["RouteTableId"]
    ec2.associate_route_table(RouteTableId=rtb_id, SubnetId=pub_subnet)
    ec2.create_route(RouteTableId=rtb_id, DestinationCidrBlock="0.0.0.0/0", GatewayId=igw_id)

    print(f"✅ IGW: {igw_id}, Route Table: {rtb_id}")
    return igw_id, rtb_id


def create_security_group(vpc_id):
    sg_id = ec2.create_security_group(
        GroupName="ubuntu-web-sg",
        Description="Allow SSH and HTTP",
        VpcId=vpc_id
    )["GroupId"]

    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {"IpProtocol": "tcp", "FromPort": 22, "ToPort": 22,
             "IpRanges": [{"CidrIp": "0.0.0.0/0"}]},
            {"IpProtocol": "tcp", "FromPort": 80, "ToPort": 80,
             "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}
        ]
    )
    print(f"✅ Security Group: {sg_id}")
    return sg_id


def launch_ec2(pub_subnet, sg_id):
    # UserData script with logging
    user_data_script = f"""#!/bin/bash
exec > /var/log/userdata.log 2>&1
set -x

apt-get update -y
apt-get install -y git nginx

systemctl enable nginx
systemctl start nginx

cd /var/www/html
rm -rf *

# Clone Git repo
git clone {GIT_REPO} site || echo "Git clone failed"

if [ -d "site" ]; then
    cp -r site/* .
fi

chown -R www-data:www-data /var/www/html
"""

    instance = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MinCount=1,
        MaxCount=1,
        UserData=user_data_script,
        NetworkInterfaces=[
            {
                "DeviceIndex": 0,
                "SubnetId": pub_subnet,
                "Groups": [sg_id],
                "AssociatePublicIpAddress": True
            }
        ]
    )

    instance_id = instance["Instances"][0]["InstanceId"]
    print(f"🚀 Launched EC2: {instance_id}")

    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])

    desc = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = desc["Reservations"][0]["Instances"][0]["PublicIpAddress"]
    print(f"🌍 Public IP: {public_ip} (Access via http://{public_ip})")
    print("📜 Check logs inside instance: /var/log/userdata.log or /var/log/cloud-init-output.log")

    return instance_id, public_ip


def main():
    vpc_id = create_vpc()
    pub_subnet, priv_subnet = create_subnets(vpc_id)
    create_igw_and_route(vpc_id, pub_subnet)
    sg_id = create_security_group(vpc_id)
    launch_ec2(pub_subnet, sg_id)


if __name__ == "__main__":
    main()
