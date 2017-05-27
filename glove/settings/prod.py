from glove.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.eyetive.com']

SECRET_KEY = os.getenv('TAXI_AMIGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('TAXI_AMIGO_DB_NAME'),
        'USER': os.getenv('TAXI_AMIGO_USER_NAME'),
        'PASSWORD': os.getenv('TAXI_AMIGO_DB_PASSWORD'),
        'HOST': os.getenv('TAXI_AMIGO_DB_HOST'),
        'PORT': os.getenv('TAXI_AMIGO_DB_PORT'),
    }
}

STATIC_ROOT = 'staticfiles'
