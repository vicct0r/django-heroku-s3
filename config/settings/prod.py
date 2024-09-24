from .base import *
import django_heroku

# CONFIGURAÇÕES PARA DESENVOLVIMENTO EM PRODUÇÃO

SECRET_KEY = 'django-insecure-za8lbt!ddvm^h@v)g)#7-2$%ttbd!f-nmvh3+jpt2lhm_3w-y*'

DEBUG = False

ALLOWED_HOSTS = ['*']

# Amazon S3 Configuração
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*'
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


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
django_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']