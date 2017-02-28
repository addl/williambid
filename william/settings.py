"""
Django settings for william project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_va_&xj(-ao%5i76ay#dg0w8ta0#l)o2yc9@x31hwtkym(syxa'

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
    # to work with paypal
    'paypal.standard.ipn',
    'williambid',
    'back_office',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # agregado para la internacionalizacion ******************************
    "django.middleware.locale.LocaleMiddleware",
)

ROOT_URLCONF = 'william.urls'

WSGI_APPLICATION = 'william.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 'django.db.backends.sqlite3',
        'NAME': 'williambid',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# import dj_database_url
#
# try:
#   database_url = os.environ["DATABASE_URL"]
# except KeyError:
#   database_url = "file:///{}".format(os.path.join(BASE_DIR, 'db.sqlite3'))
#
# DATABASES = {'default': dj_database_url.config(), 'ENGINE': "django.db.backends.mysql"}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "/var/www/williambid/static/"

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# A partir de aqui las configuraciones adicionadas por desarrolladores.

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en-us', _('English')),
    ('es-es', _('Spanish')),
    ('pt-pt', _('Portugues')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# easy mode requires set this var
PROJECT_DIR = BASE_DIR

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
#BROKER_URL = os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/New_York'

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'synchronizer': {
        'task': 'williambid.tasks.run_synchronizer',
        'schedule': timedelta(seconds=10),
        # 'args': (2, 5)
    },
    'synchronizer_main_task': {
        'task': 'williambid.tasks.run_synchronizer_main_task',
        'schedule': timedelta(seconds=5),
        # 'args': (2, 5)
    },
    'plans_manager': {
        'task': 'back_office.tasks.run_plans_manager',
        'schedule': crontab(day_of_month='1'),
        # 'args': (2, 5)
    },
    'plans_manager_short_task': {
        'task': 'back_office.tasks.run_short_periodical_tasks',
        'schedule': timedelta(seconds=10),
        # 'args': (2, 5)
    },
    'plan_zero_tasks': {
        'task': 'back_office.tasks.run_plan_zero_task',
        'schedule': crontab(minute=0, hour='*/2'),
        # 'args': (2, 5)
    }

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logs/logfile.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'back_office': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'william': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

"""
celery -A william worker -B --app=william.celery_config:app
"""

# custom setting
BOTS_ON_TREE = False