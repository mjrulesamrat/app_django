"""
Django settings for django_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_DIR = os.path.dirname(__file__)
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
#[
#    'home/django_mj/django_test/templates',
#    ]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't!%v_vd^5(ta87_ltg-!)j6bsmnup_puhb@ufw2dj58b!i1(ww'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'

TEMPLATE_DIRS = ( os.path.join(SETTINGS_PATH, 'templates'), )

#TEMPLATE_DIRS =[
 #   'home/django_mj/django_test/templates',
 #   'home/django_mj/django_test/article/templates',
#]

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

path='home/django_mj/django_test/static'

#STATIC_ROOT = path.join(PROJECT_ROOT,'static')
#STATIC_ROOT = "home/django_mj/django_test/static"
#STATIC_ROOT = "/home/django_mj/django_test/static"

#ROOT_PATH = os.path.dirname(__file__)

#STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
#STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (('assets', '/home/django_mj/django_test/static' ), )

#STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)