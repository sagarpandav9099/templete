
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-ty=(ks%vo*(n0!@dx(=%9fzjs8ns55gzmsrthh$@(_0ku6k*$3'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authuser',
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

ROOT_URLCONF = 'growupmore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'authuser' / 'templates'],
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

WSGI_APPLICATION = 'growupmore.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_RECAPTCHA_SITE_KEY = '6LdXX5gqAAAAAJWm-9E3rACC9HaZpUhtGNtAS_KP'

# Resolve issue for google recptcha in console
CSP_FRAME_ANCESTORS = ("'self'",)  # Existing directive

CSP_SCRIPT_SRC = (
    "'self'",
    "https://www.google.com/recaptcha/",
    "https://www.gstatic.com/recaptcha/",
    # Add other necessary script sources
)

CSP_FRAME_SRC = (
    "'self'",
    "https://www.google.com/recaptcha/",
    "https://www.gstatic.com/recaptcha/",
    # Add other necessary frame sources
)


# Centralize API Base URL
# API_BASE_URL = 'https://13.60.105.3'
API_BASE_URL = 'http://127.0.0.1:8000/api/'