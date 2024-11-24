import os
from django.core.files.storage import default_storage


class S3ImageUploader:
    """
    A class to handle uploading images to an S3 bucket.
    """

    def _extract_filename(self, url):
        """
        Extracts the filename from the URL.

        Args:
            url (str): URL from which to extract the filename.

        Returns:
            str: The extracted filename.
        """
        file_name = url.split("/")[-1]
        if "?" in file_name:
            file_name = file_name.split("?")[0]
        return file_name

    def store_image(self, image, obj):
        """
        Load image with GET and store response in S3 bucket.

        Args:
            url (str): URL of the image to store.

        Returns:
            str: The URL of the stored image in the S3 bucket.
        """
        file_extension = image.name.split('.')[-1]
        new_filename = f"{obj.add_id}.{file_extension}"
        s3_path = f"media/onion/images/{new_filename}"
        saved_path = default_storage.save(s3_path, image)
        file_url = default_storage.url(saved_path)

        if hasattr(image, 'close'):
            image.close()

        temp_local_path = os.path.join(default_storage.location, s3_path)
        if os.path.exists(temp_local_path):
            os.remove(temp_local_path)

        return file_url
