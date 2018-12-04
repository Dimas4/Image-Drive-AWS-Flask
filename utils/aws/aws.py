import botocore
import boto3

from app.exception.exception import FileDoesNotExist
from utils.exception.exception import BackEndError


class BackEnd:
    def __init__(self):
        self.bucket_name = 'Gallery1'
        self.s3 = boto3.client('s3', endpoint_url="http://localhost:4572")
        self.bucket = self.s3.create_bucket(Bucket=self.bucket_name)

    def get(self, key):
        try:
            s3_response_object = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        except botocore.exceptions.ClientError:
            raise FileDoesNotExist
        return s3_response_object['Body'].read()

    def post(self, name, file):
        response = self.s3.put_object(
            Bucket=self.bucket_name,
            Body=file,
            Key=name,
            ServerSideEncryption='AES256'
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise BackEndError
