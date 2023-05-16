import boto3

route_table_id = 'rtb-046eff503e9b19c28'
subnet_id = 'subnet-0ba9c737aab176a32'


ec2 = boto3.client("ec2")

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])