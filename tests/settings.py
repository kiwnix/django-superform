import warnings
warnings.simplefilter('always')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite',
    },
}

USE_I18N = True
USE_L10N = True

INSTALLED_APPS = [
    'django_compositeform',
    'tests',
]

STATIC_URL = '/static/'

SECRET_KEY = '0'

import django
if django.VERSION < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'