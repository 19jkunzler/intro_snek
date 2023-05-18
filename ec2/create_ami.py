import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-02b7a9c01ce7f9d7c',
    Name='Go to Ami')

print(response["ImageId"])