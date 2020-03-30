"""
<<<<<<< HEAD
Django settings for chat project.
Generated by 'django-admin startproject' using Django 3.0.4.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
=======
Django settings for chatapp project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'lp0^-tkp5(f(s_9w&&sgqx4igsbyec$!-s4&z0o=cl_7#9ytz$'
=======
SECRET_KEY = '8gc!s3a%b6g$v*3-7c_swt5r-9=x#r0(w&!2z4rj+a%_@_&^eu'
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'crispy_forms',
    'rest_framework',
    'main'
=======
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR + '/templates/', ],
=======
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

<<<<<<< HEAD
=======

>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, 'root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/index'
AUTH_USER_MODEL = 'main.CustomUser'
=======
>>>>>>> b8a4889b03f74d1318f7c8f3f8a85e83de3ed1bf
