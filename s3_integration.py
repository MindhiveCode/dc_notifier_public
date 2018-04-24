import boto3
import os
import datetime as DT

bucket = os.getenv('AWS_BUCKET')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

# Upload local file to S3
def upload(byte_stream, file_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    print('S3 Client Initiated')

    s3.upload_file(byte_stream, bucket, file_name)
    # s3.Bucket('review-app-jh').put_object(Key=filename, Body=data)

    print('S3 Upload Completed')

    return s3, file_name


# This wraps the upload and URL creation for the Graph
def add_and_upload_simple(byte_stream, file_name):
    s3, uploaded_file_id = upload(byte_stream, file_name)
    url = gen_URL(bucket, uploaded_file_id, s3)
    return url


# Generate URL from object ID
def gen_URL(bucket, key, s3):
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key,
            'ResponseExpires': DT.datetime.now() + DT.timedelta(days=7)
        }
    )
    return url
