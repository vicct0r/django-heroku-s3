from storages.backends.s3 import S3Storage


class StaticFileStorage(S3Storage):
    # helpers.cloudfare.storages.StaticFileStorage
    location = "static"


class MediaFileStorage(S3Storage):
    # helpers.cloudfare.storages.MediaFileStorage
    location = "media" 