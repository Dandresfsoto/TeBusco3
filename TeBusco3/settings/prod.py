from TeBusco3.settings.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {}
DATABASES['default'] = dj_database_url.config()