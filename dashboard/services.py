import datetime
import os

import boto3
from botocore.exceptions import ClientError

from dashboard import logger


class AWS:
    """
    AWS boto3 class to interact with S3 bucket
    """

    def create_session(self):
        """
        Creates AWS session
        """
        session = boto3.Session(
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            aws_session_token=os.environ.get("AWS_SESSION_TOKEN"),
        )
        return session

    def upload_to_s3(self, filename, object_name):
        """
        Upload file to s3
        """
        session = self.create_session()
        storage = session.resource("s3")
        storage.meta.client.upload_file(
            filename,
            os.environ.get("AWS_STORAGE_BUCKET_NAME"),
            object_name,
            ExtraArgs={"ContentType": "audio/mp3"},
        )

    def upload_image_to_s3(self, object_name, file_path, content_type):
        """
        to upload Image to S3
        """
        session = self.create_session()
        storage = session.resource("s3")
        storage.meta.client.put_object(
            Body=object_name,
            Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"),
            Key=file_path,
            ContentType=content_type,
        )
        return f"{os.getenv('AWS_PUBLIC_BUCKET_URL')}{file_path}"

    def delete_file(self, object_name):
        """
        Deletes a file from s3
        """
        session = self.create_session()
        storage = session.resource("s3")
        try:
            storage.meta.client.delete_object(
                Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"), Key=object_name
            )
            return True
        except Exception as e:
            logger.exception(msg=str(e), exc_info=True)
            return False

    def check_file_exists(self, object_name):
        """
        Check if the file exists or not on S3
        """
        session = self.create_session()
        storage = session.resource("s3")
        try:
            storage.meta.client.head_object(
                Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"), Key=object_name
            )
        except ClientError as e:
            return int(e.response["Error"]["Code"]) != 404
        return True

    def list_files(self):
        """
        Lista all the files in s3 bucket
        """
        session = self.create_session()
        storage = session.resource("s3")

        curr_date = datetime.datetime.now()
        try:
            response = storage.meta.client.list_objects_v2(
                Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"), Prefix="media/clips/"
            )
            clips_list = []
            for clip in response["Contents"]:
                try:
                    clip_date = clip["LastModified"].replace(tzinfo=None)
                    time_difference = curr_date - clip_date
                    if time_difference.days < 15:
                        mp3_clip = clip["Key"].split("/")[2].split(".")[0]
                        clips_list.append(mp3_clip)
                except Exception as e:
                    logger.exception(msg=str(e), exc_info=True)
        except ClientError as e:
            return int(e.response["Error"]["Code"]) != 404

        return clips_list

    def download_from_s3(self, object_name, local_file_path):
        """
        Download a file from S3 to the local file system
        """
        session = self.create_session()
        storage = session.resource("s3")
        try:
            storage.meta.client.download_file(
                Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"),
                Key=object_name,
                Filename=local_file_path,
            )
            return True
        except ClientError:
            return False
