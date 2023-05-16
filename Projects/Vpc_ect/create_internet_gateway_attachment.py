import boto3

internet_gateway_id = 'igw-0395e8d2689adf324'
vpc_id = 'vpc-0b726695a6682b67a'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id)
