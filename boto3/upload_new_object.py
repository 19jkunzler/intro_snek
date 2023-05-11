import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket='kunzler-boto3-05112023', Key='test_text_string.txt', Body="You underestimate my power", ContentType='text/plain')
     