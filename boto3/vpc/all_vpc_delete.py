import boto3
import time

def get_all_regions():
    """Fetch all AWS regions (requires one region for initial call)."""
    ec2 = boto3.client("ec2", region_name="us-east-1")
    regions = ec2.describe_regions(AllRegions=True)["Regions"]
    return [r["RegionName"] for r in regions]

def delete_vpc_and_resources(region):
    print(f"\n--- Checking region: {region} ---")
    ec2 = boto3.client("ec2", region_name=region)
    elb = boto3.client("elb", region_name=region)
    elbv2 = boto3.client("elbv2", region_name=region)
    rds = boto3.client("rds", region_name=region)

    vpcs = ec2.describe_vpcs()["Vpcs"]

    for vpc in vpcs:
        vpc_id = vpc["VpcId"]
        if vpc.get("IsDefault", False):
            print(f"Skipping default VPC: {vpc_id}")
            continue

        print(f"\nFound VPC: {vpc_id} - Cleaning up resources...")

        # Terminate EC2 Instances
        instances = ec2.describe_instances(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])
        instance_ids = [i["InstanceId"] for r in instances["Reservations"] for i in r["Instances"]]
        if instance_ids:
            print(f"  Terminating EC2 Instances: {instance_ids}")
            ec2.terminate_instances(InstanceIds=instance_ids)
            waiter = ec2.get_waiter("instance_terminated")
            waiter.wait(InstanceIds=instance_ids)

        # Delete NAT Gateways
        nat_gateways = ec2.describe_nat_gateways(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["NatGateways"]
        for nat in nat_gateways:
            print(f"  Deleting NAT Gateway: {nat['NatGatewayId']}")
            ec2.delete_nat_gateway(NatGatewayId=nat["NatGatewayId"])
        if nat_gateways:
            time.sleep(60)  # NAT takes time to delete

        # Delete Classic Load Balancers (ELB)
        lbs = elb.describe_load_balancers()["LoadBalancerDescriptions"]
        for lb in lbs:
            if lb["VPCId"] == vpc_id:
                print(f"  Deleting ELB: {lb['LoadBalancerName']}")
                elb.delete_load_balancer(LoadBalancerName=lb["LoadBalancerName"])

        # Delete Application/Network Load Balancers (ELBv2)
        lbs_v2 = elbv2.describe_load_balancers()["LoadBalancers"]
        for lb in lbs_v2:
            if lb["VpcId"] == vpc_id:
                print(f"  Deleting ELBv2: {lb['LoadBalancerArn']}")
                elbv2.delete_load_balancer(LoadBalancerArn=lb["LoadBalancerArn"])

        # Delete RDS Instances in VPC
        dbs = rds.describe_db_instances()["DBInstances"]
        for db in dbs:
            if db["DBSubnetGroup"]["VpcId"] == vpc_id:
                print(f"  Deleting RDS DB Instance: {db['DBInstanceIdentifier']}")
                rds.delete_db_instance(
                    DBInstanceIdentifier=db["DBInstanceIdentifier"],
                    SkipFinalSnapshot=True,
                    DeleteAutomatedBackups=True
                )

        # Delete Subnets
        subnets = ec2.describe_subnets(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["Subnets"]
        for subnet in subnets:
            print(f"  Deleting Subnet: {subnet['SubnetId']}")
            ec2.delete_subnet(SubnetId=subnet["SubnetId"])

        # Detach & Delete Internet Gateways
        igws = ec2.describe_internet_gateways(Filters=[{"Name": "attachment.vpc-id", "Values": [vpc_id]}])["InternetGateways"]
        for igw in igws:
            igw_id = igw["InternetGatewayId"]
            print(f"  Detaching & Deleting IGW: {igw_id}")
            ec2.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
            ec2.delete_internet_gateway(InternetGatewayId=igw_id)

        # Delete Route Tables (except main)
        rts = ec2.describe_route_tables(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["RouteTables"]
        for rt in rts:
            associations = rt.get("Associations", [])
            if any(assoc.get("Main") for assoc in associations):  # skip main RT
                continue
            print(f"  Deleting Route Table: {rt['RouteTableId']}")
            ec2.delete_route_table(RouteTableId=rt["RouteTableId"])

        # Delete Security Groups (skip default)
        sgs = ec2.describe_security_groups(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["SecurityGroups"]
        for sg in sgs:
            if sg["GroupName"] == "default":
                continue
            print(f"  Deleting Security Group: {sg['GroupId']}")
            ec2.delete_security_group(GroupId=sg["GroupId"])

        # Delete Network ACLs (skip default)
        acls = ec2.describe_network_acls(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["NetworkAcls"]
        for acl in acls:
            if acl.get("IsDefault"):
                continue
            print(f"  Deleting Network ACL: {acl['NetworkAclId']}")
            ec2.delete_network_acl(NetworkAclId=acl["NetworkAclId"])

        # Delete VPC Endpoints
        endpoints = ec2.describe_vpc_endpoints(Filters=[{"Name": "vpc-id", "Values": [vpc_id]}])["VpcEndpoints"]
        for ep in endpoints:
            print(f"  Deleting VPC Endpoint: {ep['VpcEndpointId']}")
            ec2.delete_vpc_endpoints(VpcEndpointIds=[ep["VpcEndpointId"]])

        # Finally Delete VPC
        print(f"  Deleting VPC: {vpc_id}")
        ec2.delete_vpc(VpcId=vpc_id)

def main():
    regions = get_all_regions()
    for region in regions:
        try:
            delete_vpc_and_resources(region)
        except Exception as e:
            print(f"Error in region {region}: {str(e)}")

if __name__ == "__main__":
    main()
