# Justin Heinrichs (qtr4sk)
import boto3
import requests
import logging
from botocore.exceptions import ClientError

def create_presigned_url(bucket_name, object_name, expiration=60):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None

    return response

url = 'https://logicmojo.com/assets/dist/new_pages/images/data-science-intro.gif'
local_name = 'gif'

response = requests.get(url)
with open(local_name, 'wb') as file:
    file.write(response.content)

s3 = boto3.client('s3', region_name="us-east-1")

bucket_name = 'ds2002-qtr4sk'
object_name = local_name

s3.upload_file(local_name, bucket_name, object_name)

url = create_presigned_url(bucket_name, object_name)
if url is not None:
    print("Presigned URL: " + url)