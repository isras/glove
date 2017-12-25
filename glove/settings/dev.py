from glove.settings.base import *

INSTALLED_APPS += (
    'debug_toolbar',
)

SECRET_KEY = os.environ.get("TAXIAMIGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
