from glove.settings.base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taxi_amigo',
        'USER': 'postgres',
        'PASSWORD': 'Eyetive@2016',  # os.getenv('PLATZI_DB_PASSWORD'),
        'HOST': '',  # os.getenv('PLATZI_DB_HOST'),
        'PORT': '',  # os.getenv('PLATZI_DB_PORT'),
    }
}

STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/'
