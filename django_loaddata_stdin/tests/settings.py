"""
Test apps settings.
"""

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMIN = ('foo@bar')
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'django_loaddata_stdin.tests.testapp.urls'
SECRET_KEY = "it's a secret to everyone"
SITE_ID = 1
INSTALLED_APPS = (
    'django_loaddata_stdin',
    'django_loaddata_stdin.tests.testapp',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
