# -*- encoding: utf-8 -*-
from os.path import abspath, dirname, basename, join, normpath
from sys import path
from django.core.exceptions import ImproperlyConfigured
import json


BASE_DIR = dirname(dirname(abspath(__file__)))
path.append(BASE_DIR)

SITE_ROOT = dirname(BASE_DIR)
# Site name:
SITE_NAME = basename(BASE_DIR)

with open(normpath(join(BASE_DIR, 'settings')) + "/secrets.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} enviroment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = [('Jon', 'jon@iddeasmkt.com')]


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ckeditor',
    'sorl.thumbnail',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cmgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmgo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ######### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION

# ######### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

STATICFILES_DIRS = (
    # normpath(join(SITE_ROOT, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
FILE_UPLOAD_PERMISSIONS = 0o644

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [
                'Undo', 'Redo',
                '-', 'Bold', 'Italic', 'Underline',
                '-', 'Link', 'Unlink', 'Anchor',
                '-', 'Format', 'RemoveFormat',
                '-', 'SpellChecker', 'Scayt',
                '-', 'Maximize',
                '-', 'JustifyLeft', 'JustifyCenter',
                'JustifyRight', 'JustifyBlock',
            ],
            [
                'HorizontalRule',
                '-', 'Image',
                '-', 'Table',
                '-', 'BulletedList', 'NumberedList',
                '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                '-', 'SpecialChar',
                '-', 'Source',
                '-', 'About',
            ]
        ],
        'width': -1,
        'height': 300,
        'toolbarCanCollapse': False,
        'extraAllowedContent': 'iframe[*]',
    }
}

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.AllowAny',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    #     # 'rest_framework.authentication.SessionAuthentication',

    # )

}

# twitter
CONST_USER_TWITTER = get_secret("CONST_USER_TWITTER")
CONSUMER_KEY_TWITTER = get_secret("CONSUMER_KEY_TWITTER")
CONSUMER_SECRET_TWITTER = get_secret("CONSUMER_SECRET_TWITTER")
ACCESS_TOKEN_TWITTER = get_secret("ACCESS_TOKEN_TWITTER")
ACCESS_TOKEN_SECRET_TWITTER = get_secret("ACCESS_TOKEN_SECRET_TWITTER")

# facebook
CONST_USER_FACEBOOK = get_secret("CONST_USER_FACEBOOK")
EXTENDED_TOKEN_FACEBOOK = get_secret("EXTENDED_TOKEN_FACEBOOK")


CKEDITOR_UPLOAD_PATH = "uploads/"


JET_SIDE_MENU_COMPACT = True

JET_DEFAULT_THEME = 'default'

JET_THEMES = [
{
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
