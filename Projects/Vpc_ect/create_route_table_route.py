import boto3

route_table_id = 'rtb-046eff503e9b19c28'
internet_gateway_id = 'igw-0395e8d2689adf324'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
