from glove.settings.base import *

SECRET_KEY = '8911-b0bayen76)flqc3muy+u1fvt$&op=oqtm^+@bfu9a(v1x'

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}