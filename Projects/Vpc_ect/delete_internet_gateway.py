import boto3

internet_gateway_id = 'igw-0395e8d2689adf324'


ec2 = boto3.client('ec2')


ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)

