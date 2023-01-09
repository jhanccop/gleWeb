from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# get_secret("SECRET_KEY")

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR.child('db.sqlite3')
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("USER"),
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': 'localhost',
        'PORT': '3306'
    },
    'OPTIONS': {
     "init_command": "SET foreign_key_checks = 0;",
     },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]
