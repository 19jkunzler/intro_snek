import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='kunzler-boto3-05112023', 
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    })
   
print(response)