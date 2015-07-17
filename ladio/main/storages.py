from storages.backends.s3boto import S3BotoStorage
from django.conf import settings

class StaticRootS3BotoStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaRootS3BotoStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
