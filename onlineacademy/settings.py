import os
from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env()
# Read .env file, if it exists
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/ref/settings/

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')  # Load from environment variable or .env file
DEBUG = env.bool('DEBUG', default=False)  # Load from environment or default to False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # If using Django sites framework
    'rest_framework',  # For building APIs (optional)
    'rest_framework.authtoken',  # For token authentication (optional)
    'oacademyapp',  # Your app
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

ROOT_URLCONF = 'onlineacademy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'onlineacademy.wsgi.application'

# Database configuration (using environment variable for DB URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'onlineacademy',
        'USER': 'onlineacademy',
        'PASSWORD': 'Pa$$w0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session settings (optional)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the database

# User authentication settings
AUTH_USER_MODEL = 'auth.User'  # Default User model (can be customized)

# Email backend for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')  # Use Gmail for sending emails
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='your-email-password')

# Third-party API integrations (optional)

# Rest Framework settings (if using DRF)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Django-Environ configuration
# This will load variables from the .env file for sensitive data like SECRET_KEY, DATABASE_URL, etc.
env_file = BASE_DIR / '.env'
if env_file.exists():
    environ.Env.read_env(str(env_file))
    
DJANGO_SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE', default='onlineacademy.settings')
DJANGO_ENV = env('DJANGO_ENV', default='development')  # You can set a default value here
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')  # Default to 'development' if not set

if DJANGO_ENV == 'development':
    # Development settings
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

elif DJANGO_ENV == 'production':
    # Production settings
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'prod_db',
            'USER': 'prod_user',
            'PASSWORD': 'prod_password',
            'HOST': 'prod_host',
            'PORT': '5432',
        }
    }
    ALLOWED_HOSTS = ['yourproductiondomain.com']


# CORS settings if you want to enable cross-origin requests
CORS_ORIGIN_ALLOW_ALL = True  # Set to False and configure specific origins in production

