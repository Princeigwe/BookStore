"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# for HEROKU
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True ## PROTECTS FROM CROSS SITE SCRIPTING ATTACK
    X_FRAME_OPTIONS='DENY' # SECURES FROM CLICKJACKING ATTACK
    SECURE_SSL_REDIRECT=True ## HTTPS security
    SECURE_HSTS_SECONDS = 3600 
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
    SECURE_HSTS_PRELOAD = True 
    SECURE_CONTENT_TYPE_NOSNIFF = True 
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') ## to prevent redirects


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('NEW_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = int(os.environ.get('DEBUG', default = 0))
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0', 'bookstorecomm.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    #third party apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken', # rest framework for generating the token in the server
    'dj_rest_auth', # django restframework authentication app
    'dj_rest_auth.registration', # django restframework authentication app for registration
    'drf_yasg', # rest app for api documentation
    'django_dropbox_storage', # django dropbox storage... forked version
    
    
    
    #local apps
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payments.apps.PaymentsConfig',
    'wishlist.apps.WishlistConfig',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'skydata',
        'PASSWORD': '12345678',
        'HOST':  'db',
        'PORT': 5432
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]

# django-allauth config section
SITE_ID = 2

AUTH_USER_MODEL = "users.CustomUser"
LOGIN_REDIRECT_URL = 'pages:home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'pages:home' ## django-allauth configuration



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # configuration for using django default authentication
    'allauth.account.auth_backends.AuthenticationBackend', # configuration for django-allauth authentication
]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



ACCOUNT_SESSION_REMEMBER = False ## django-allauth to remember login session
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True # django-allauth to show password twice on signup form
ACCOUNT_USERNAME_REQUIRED = True ## username required for signup
ACCOUNT_UNIQUE_EMAIL = True # django-allauth to allow unique emails for signup
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2 # expiration days for email confirmation
ACCOUNT_UNIQUE_EMAIL = True

SOCIALACCOUNT_QUERY_EMAIL = True

# ACCOUNT_EMAIL_VERIFICATION="mandatory" 
ACCOUNT_SIGNUP_REDIRECT_URL= 'account_login'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

DEFAULT_FROM_EMAIL = 'admin@bookstore.com' 


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# cart session key
CART_SESSION_ID = 'cart'


# FLUTTERWAVE RAVE KEYS
RAVE_TEST_PUBLIC_KEY = os.environ.get('FLUTTERWAVE_PUBLIC_TEST_KEY')
RAVE_TEST_SECRET_KEY = os.environ.get('FLUTTERWAVE_SECRET_TEST_KEY')

RAVE_LIVE_PUBLIC_KEY = os.environ.get('FLUTTERWAVE_LIVE_PUBLIC_KEY')
RAVE_LIVE_SECRET_KEY = os.environ.get('FLUTTERWAVE_LIVE_SECRET_KEY')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
}

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#DROPBOX STORAGE
DEFAULT_FILE_STORAGE = 'django_dropbox_storage.storage.DropboxStorage'
#DROPBOX_CONSUMER_KEY = os.environ.get('DROPBOX_CONSUMER_KEY')
DROPBOX_CONSUMER_KEY = 'ankyfxieedhdct1'
#DROPBOX_CONSUMER_SECRET = os.environ.get('DROPBOX_CONSUMER_SECRET')
DROPBOX_CONSUMER_SECRET = '6cyumci8ijnfchc'

#DEFAULT_FILE_STORAGE = 'django_dropbox_storage.storage.DropboxStorage'
DROPBOX_ACCESS_TOKEN='FQzCtiH8ufAAAAAAAAAAE9eBusK1bSXKvpF_RdjWjRM'
DROPBOX_ROOT_FOLDER = '/Public'
## ELASTICSEARCH DSL SETTING
# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': os.getenv("ELASTICSEARCH_DSL_HOSTS", 'localhost:9200')
#     },
# }

# Haystack setting
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack',
#     },
# }

