FILE=$1
BUCKET=$2
EXPIRATION=$3

aws s3 cp "$FILE" s3://$BUCKET/
aws s3 presign --expires-in $EXPIRATION s3://$BUCKET/$FILE
