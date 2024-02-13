# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]


# Application definition
SITE_ID = 2

# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # # OAuth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'apps.users',
    'rest_framework',





    'apps.home',  # Enable the inner home (home)
    'apps.dash',

    'django_plotly_dash.apps.DjangoPlotlyDashConfig', #DY
    'dpd_static_support', #DY
    # 'subscriptions.apps.SubscriptionsConfig', #DY
    'apps.subscriptions',
    # 'app.subscriptions.apps.SubscriptionsConfig', #DY

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_plotly_dash.middleware.BaseMiddleware',#DY
    'django_plotly_dash.middleware.ExternalRedirectionMiddleware', #DY

]


PLOTLY_COMPONENTS = [
    'dpd_static_support', #DY
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',
    'dpd_components'    
]



ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'apps.subscriptions.context_processors.subscription_status',#DY
            ],
        },
    },
]

X_FRAME_OPTIONS = 'SAMEORIGIN'#DY

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


#############################################################
#############################################################


# ALLOWED_HOSTS = ['localhost', '127.0.0.1']


STRIPE_PUBLISHABLE_KEY = 'pk_test_7GkW4sC4fU3LoLiKRfUKvCRc'
STRIPE_SECRET_KEY = 'sk_test_jq0oD1JKfQTuFEM3NL145Wps'
STRIPE_PRICE_ID = 'price_1OhfK8HazaBU80KQZlz33YLD'
STRIPE_ENDPOINT_SECRET = 'whsec_06664617082abc873651b86b10bd4715546aedad9f9800def0ce2dbf8c572828'



##################### OAuth


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

LOGIN_REDIRECT_URL = '/subscription/'
LOGOUT_REDIRECT_URL = '/'
  
# DY

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


ACCOUNT_EMAIL_VERIFICATION = 'none'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SOCIALACCOUNT_PROVIDERS = {
"google": {
    "APP": {
        "client_id": "1050681226172-1bde5vtrb5ivvk4733b9hhkh4fmv9g3u.apps.googleusercontent.com",
        "secret": "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",
    },
},
}