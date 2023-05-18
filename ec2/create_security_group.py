import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='Security group from boto3',
    GroupName='boto3-security-group',
    VpcId='vpc-08672886899d1391d',
)

print(response["GroupId"])