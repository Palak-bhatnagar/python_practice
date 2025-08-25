import boto3
import time

REGION = "us-east-1"
ec2 = boto3.client("ec2", region_name=REGION)


def delete_ec2_instances(vpc_id):
    instances = ec2.describe_instances(
        Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
    )["Reservations"]

    instance_ids = []
    for res in instances:
        for inst in res["Instances"]:
            if inst["State"]["Name"] != "terminated":
                instance_ids.append(inst["InstanceId"])

    if instance_ids:
        print(f"🛑 Terminating instances: {instance_ids}")
        ec2.terminate_instances(InstanceIds=instance_ids)
        waiter = ec2.get_waiter("instance_terminated")
        waiter.wait(InstanceIds=instance_ids)
    else:
        print("✅ No EC2 instances found.")


def delete_security_groups(vpc_id):
    sgs = ec2.describe_security_groups(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["SecurityGroups"]

    for sg in sgs:
        if sg["GroupName"] != "default":  # don't delete default SG
            try:
                ec2.delete_security_group(GroupId=sg["GroupId"])
                print(f"✅ Deleted Security Group: {sg['GroupId']}")
            except Exception as e:
                print(f"⚠️ Could not delete SG {sg['GroupId']}: {e}")


def delete_igw(vpc_id):
    igws = ec2.describe_internet_gateways(
        Filters=[{"Name": "attachment.vpc-id", "Values": [vpc_id]}]
    )["InternetGateways"]

    for igw in igws:
        igw_id = igw["InternetGatewayId"]
        try:
            ec2.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
            ec2.delete_internet_gateway(InternetGatewayId=igw_id)
            print(f"✅ Deleted IGW: {igw_id}")
        except Exception as e:
            print(f"⚠️ Could not delete IGW {igw_id}: {e}")


def delete_route_tables(vpc_id):
    rtbs = ec2.describe_route_tables(
        Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
    )["RouteTables"]

    for rtb in rtbs:
        associations = rtb.get("Associations", [])
        for assoc in associations:
            if not assoc.get("Main", False):
                try:
                    ec2.disassociate_route_table(AssociationId=assoc["RouteTableAssociationId"])
                except:
                    pass
        try:
            ec2.delete_route_table(RouteTableId=rtb["RouteTableId"])
            print(f"✅ Deleted Route Table: {rtb['RouteTableId']}")
        except Exception as e:
            print(f"⚠️ Could not delete RTB {rtb['RouteTableId']}: {e}")


def delete_subnets(vpc_id):
    subnets = ec2.describe_subnets(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["Subnets"]

    for subnet in subnets:
        try:
            ec2.delete_subnet(SubnetId=subnet["SubnetId"])
            print(f"✅ Deleted Subnet: {subnet['SubnetId']}")
        except Exception as e:
            print(f"⚠️ Could not delete Subnet {subnet['SubnetId']}: {e}")


def delete_vpc(vpc_id):
    try:
        ec2.delete_vpc(VpcId=vpc_id)
        print(f"🎉 Deleted VPC: {vpc_id}")
    except Exception as e:
        print(f"⚠️ Could not delete VPC {vpc_id}: {e}")


def main(vpc_id):
    delete_ec2_instances(vpc_id)
    delete_security_groups(vpc_id)
    delete_igw(vpc_id)
    delete_route_tables(vpc_id)
    delete_subnets(vpc_id)
    delete_vpc(vpc_id)


if __name__ == "__main__":
    # 🔴 Replace with your VPC ID created earlier
    VPC_ID = "vpc-06e55159713432db2"
    main(VPC_ID)
