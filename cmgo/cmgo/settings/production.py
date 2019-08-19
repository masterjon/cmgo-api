from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True