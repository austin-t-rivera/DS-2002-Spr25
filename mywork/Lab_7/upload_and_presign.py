import boto3
import requests

bucket = "ds2002-zxr2ex"
url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
filename = "example.png"
expires_in = 300

r = requests.get(url)
with open(filename, 'wb') as f:
    f.write(r.content)

s3 = boto3.client('s3', region_name='us-east-1')
s3.upload_file(filename, bucket, filename)

presigned = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': filename},
    ExpiresIn=expires_in
)

print("Presigned URL:")
print(presigned)
