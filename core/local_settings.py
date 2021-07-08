import os

from core.settings import BASE_DIR, DATA_DIR

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "gladkikhit@mail.ru"
EMAIL_HOST_PASSWORD = "ItItIt254004"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '3+=mvj3-4&1(2%6jg%88zzv=c3&%t&&2&0j27p=40bc))d-v%5'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': os.path.join(DATA_DIR, 'files', 'project.db'),
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}