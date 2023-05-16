import boto3

subnet_id = 'subnet-0ba9c737aab176a32'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)
