import json
import os

import botocore
import boto3

from app.exception.exception import ImageDoesNotExist
from utils.exception.exception import BackEndError


class BackEnd:
    def __init__(self):
        self.bucket_name = 'Gallery1'
        self.s3 = boto3.client('s3', endpoint_url="http://localhost:4572")
        self.s3.create_bucket(Bucket=self.bucket_name)

    def get(self, key):
        s3_response_object = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        return s3_response_object['Body'].read()

    def post(self, name, file):
        self.s3.upload_file(name, self.bucket_name, name)
