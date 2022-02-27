from operator import attrgetter
import boto3
import botocore
import sys

s3 = boto3.resource('s3')

def main(BUCKET_NAME, KEY):
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'uploads/'+KEY)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


if __name__ == "__main__":
    args = sys.argv[1:3]
    main(args[0], args[1])
