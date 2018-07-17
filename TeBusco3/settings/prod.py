from TeBusco3.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {}
DATABASES['default'] = dj_database_url.config()