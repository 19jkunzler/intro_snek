import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0598503e4aa54b402',
)

print(response)

# make sure the securtiy group is not attached to any instances otherwise it will not delete