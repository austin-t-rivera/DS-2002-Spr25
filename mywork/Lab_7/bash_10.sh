#!/bin/bash

# arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_in_seconds>"
    exit 1
fi

# Assigning args to vars
FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Uploading file to bucket
aws s3 cp "$FILE" "s3://$BUCKET_NAME/"

# Generating a URL
URL=$(aws s3 presign "s3://$BUCKET_NAME/$(basename "$FILE")" --expires-in "$EXPIRATION")

# result
if [ $? -eq 0 ]; then
    echo "File uploaded successfully!"
    echo "Pre-signed URL: $URL"
else
    echo "Error: Failed to generate pre-signed URL."
    exit 2
fi
