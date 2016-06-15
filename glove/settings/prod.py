from glove.settings.base import *

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.getenv('GLOVE_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('GLOVE_DB_NAME'),
        'USER': os.getenv('GLOVE_USER_NAME'),
        'PASSWORD': os.getenv('GLOVE_DB_PASSWORD'),
        'HOST': os.getenv('GLOVE_DB_HOST'),
        'PORT': os.getenv('GLOVE_DB_PORT'),
    }
}

STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/'
