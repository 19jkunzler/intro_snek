import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='kunzler-boto3-05112023')

for content in response