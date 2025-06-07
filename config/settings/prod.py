from .base import *

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['.fly.dev']

CLOUDFLARE_R2_BUCKET=env("CLOUDFLARE_R2_BUCKET")
CLOUDFLARE_R2_ACESS_KEY=env("CLOUDFLARE_R2_ACESS_KEY")
CLOUDFLARE_R2_SECRET_KEY=env("CLOUDFLARE_R2_SECRET_KEY")
CLOUDFLARE_R2_BUCKET_ENDPOINT=env("CLOUDFLARE_R2_BUCKET_ENDPOINT")

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name": CLOUDFLARE_R2_BUCKET,
    "access_key": CLOUDFLARE_R2_ACESS_KEY,
    "secret_key": CLOUDFLARE_R2_SECRET_KEY,
    "endpoint_url": CLOUDFLARE_R2_BUCKET_ENDPOINT,
    "default_acl": "public-read",
    "signature_version": "s3v4"
}

# Django 4.2 staticfiles config
# Estamos mandando em dois locais do mesmo bucket
# Em caso de MEDIA muito grande, é uma boa ideia usar buckets diferentes
STORAGES = {
    "default": {
        "BACKEND": "helpers.cloudfare.storages.MediaFileStorage", # django-storages[S3]
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS
    }, # default -> user file field uploads
    "staticfiles": {
        "BACKEND": "helpers.cloudfare.storages.StaticFileStorage", # django-storages
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS
    }

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}