from .base import *
import os

# CONFIGURAÇÕES PARA DESENVOLVIMENTO LOCALHOST

SECRET_KEY = 'django-insecure-za8lbt!ddvm^h@v)g)#7-2$%ttbd!f-nmvh3+jpt2lhm_3w-y*'

DEBUG = True

ALLOWED_HOSTS = ['*']


# STATIC & MEDIA LOCAL CONFIG
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
