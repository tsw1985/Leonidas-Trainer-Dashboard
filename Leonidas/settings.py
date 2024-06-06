"""
Django settings for Leonidas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


"""
HOW TO RUN THE PROJECT:
    python manage.py runserver
    crear base de datos : python manage.py syncdb
"""

"""
INSTALATION PACKAGES:
    apt-get install libmysqlclient-dev :
    pip install MySQL-python
    pip install simplejson
    easy_install wadofstuff-django-serializers
    pip uninstall simplejson ( si esta instalado )
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# una vez se instale el paquete hay que desinstalar el paquete simplejson
# con pip uninstall simplejson y activar el nuevo
# el simple json es una mierda y no pone los modelos en las relaciones FK
SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '89vt7-im5bcjpi2twc*3k)65&i!t_spe0$&)d50)k7y1^fxr3i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Plantillas
TEMPLATE_DIRS = ('BackEnd/templates',)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'BackEnd',
    'FrontEnd',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Leonidas.urls'

WSGI_APPLICATION = 'Leonidas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LeonidasTrainer',
        'USER': 'root',
        'PASSWORD': 'shadow',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
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

import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

print 'RUTA PROYECTO %s' % RUTA_PROYECTO

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(RUTA_PROYECTO, 'static'),
)



# Redireccion cuando se loguea el usuario
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/'