import os
import datetime

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/')

SECRET_KEY = '&vcygl3^87=m&ev6o+wpk#lcyij6mj)7dz(zc10j-w60e500p5'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'trip_lister.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
    'django_evolution',
    'django_extensions',
    
    'trips',
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

try:
    from settings_local import *
except:
    pass
