import requests
import boto3
import argparse

# Download the file
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

# Upload the file to S3
def upload_to_s3(filename, bucket, object_name):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket, object_name)
    print(f"Uploaded {filename} to S3 bucket {bucket} as {object_name}")

# Generate the presigned URL
def generate_presigned_url(bucket, object_name, expires_in=3600):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': object_name},
        ExpiresIn=expires_in
    )
    return url

def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Download a file, upload it to S3, and generate a presigned URL.")
    parser.add_argument('url', help="URL of the file to download")
    parser.add_argument('bucket', help="S3 bucket name")
    parser.add_argument('object_name', help="Object name for the file in S3")
    parser.add_argument('--expires_in', type=int, default=3600, help="Expiration time for presigned URL (default 3600 seconds)")
    
    args = parser.parse_args()

    # Download the file
    filename = "downloaded_file.gif"
    download_file(args.url, filename)

    # Upload to S3
    upload_to_s3(filename, args.bucket, args.object_name)

    # Generate presigned URL
    url = generate_presigned_url(args.bucket, args.object_name, args.expires_in)
    print(f"Presigned URL (expires in {args.expires_in} seconds): {url}")

if __name__ == "__main__":
    main()
