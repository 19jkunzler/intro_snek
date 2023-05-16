import boto3

vpc_id = 'vpc-0b726695a6682b67a'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

