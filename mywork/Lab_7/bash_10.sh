#!/bin/bash

# arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_in_seconds>"
    exit 1
fi

# Assign input arguments to variables
FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 2
fi

# Upload the file to the S3 bucket 
aws s3 cp "$FILE" "s3://$BUCKET_NAME/"

# Check if upload was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to upload file to S3 bucket."
    exit 3
fi

# Generate a pre-signed URL that expires in the given expiration time (default: 604800 seconds)
URL=$(aws s3 presign "s3://$BUCKET_NAME/$(basename "$FILE")" --expires-in "$EXPIRATION")

# Check if the URL generation was successful
if [ $? -eq 0 ]; then
    echo "File uploaded successfully!"
    echo "Pre-signed URL (expires in $EXPIRATION seconds): $URL"
else
    echo "Error: Failed to generate pre-signed URL."
    exit 4
fi
