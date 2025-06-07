from .base import *
import os

# CONFIGURAÇÕES PARA DESENVOLVIMENTO LOCALHOST

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*']


# STATIC & MEDIA LOCAL CONFIG
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
