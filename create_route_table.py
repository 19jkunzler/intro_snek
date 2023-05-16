import boto3

ec2 = boto3.client('ec2')

vpc_id = "vpc-0b726695a6682b67a"

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])