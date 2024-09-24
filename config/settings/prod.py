from .base import *
import django_heroku
import dj_database_url
import os

# CONFIGURAÇÕES PARA DESENVOLVIMENTO EM PRODUÇÃO

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

# heroku database settings
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# AWS S3 SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    }
}


# Heroku Loggin
DEBUG_PROPAGATE_EXCEPTIONS = True

# Esta configuração de Logging serve para que eu não veja os erros do Django no log do Heroku
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefm': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}


# Heroku settings
django_heroku.settings(locals(), staticfiles=False)

