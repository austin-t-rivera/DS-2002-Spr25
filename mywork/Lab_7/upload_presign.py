
import boto3 

import requests 

bucket_name = "ds2002-eku2ec"
object_name = "beach.jpg"
url = "https://www.surfertoday.com/images/stories/beach-sunset.jpg"
expires_in = 604800


r = requests.get(url)
open(object_name, "wb").write(r.content) 

s3 = boto3.client("s3", region_name="us-east-1")


resp = s3.put_object(
	Body = open(object_name, "rb"),
	Bucket = bucket_name, 
	Key = object_name)


presigned_url = s3.generate_presigned_url(
	"get_object", 
	Params={"Bucket": bucket_name, "Key": object_name},
	ExpiresIn=expires_in)

print("Presigned URL:", presigned_url)
