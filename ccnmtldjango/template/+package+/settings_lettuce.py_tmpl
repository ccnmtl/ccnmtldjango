# flake8: noqa
from settings_shared import *
import sys
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lettuce.db',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        }
    }

if 'migrate' not in sys.argv:
    INSTALLED_APPS.append('lettuce.django')

BROWSER = 'Chrome'
if os.environ.get('SELENIUM_BROWSER', False):
    # it's handy to be able to set this from an
    # environment variable
    BROWSER = os.environ.get('SELENIUM_BROWSER')
