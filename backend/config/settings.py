import os
from pathlib import Path

# ------------------------------
#   BASE DIRECTORY
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
#   SECURITY
# ------------------------------
SECRET_KEY = 'dev-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# ------------------------------
#   INSTALLED APPS
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Your apps
    'core',
]

AUTHENTICATION_BACKENDS = [
    'core.backends.EmailBackend',  # our custom backend
    'django.contrib.auth.backends.ModelBackend',  # fallback
]


# Optional: redirect after login
LOGIN_REDIRECT_URL = '/profile/'  # after login, go to profile page
LOGOUT_REDIRECT_URL = '/'        # after logout, go to landing page

# ------------------------------
#   MIDDLEWARE
# ------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# ------------------------------
#   URL CONFIG
# ------------------------------
ROOT_URLCONF = 'config.urls'

# ------------------------------
#   TEMPLATES
# ------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ------------------------------
#   WSGI
# ------------------------------
WSGI_APPLICATION = 'config.wsgi.application'

# ------------------------------
#   DATABASE
# ------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------
#   PASSWORD VALIDATORS
# ------------------------------
AUTH_PASSWORD_VALIDATORS = []

# ------------------------------
#   INTERNATIONALIZATION
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
#   STATIC & MEDIA FILES
# ------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------
#   REST FRAMEWORK
# ------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

ALLOWED_HOSTS = [
    'aakash02.pythonanywhere.com',
    'www.aakash02.pythonanywhere.com',
]


# ------------------------------
#   CORS
# ------------------------------
CORS_ALLOW_ALL_ORIGINS = True

# ------------------------------
#   STRIPE KEYS
# ------------------------------
STRIPE_SECRET_KEY = os.environ.get(
    'STRIPE_SECRET_KEY',
    'sk_test_51SUWHsK8fYvT5V5ZkfvJ9JqglS5GTHe5kUmrHSEhbeg2TdJIEUYy8a9DQx0JPfG3JSIC1ydxowjCTmTUJpSyh0Qo00fDi19DJl'  # Replace with your Stripe test secret key
)

STRIPE_PUBLIC_KEY = os.environ.get(
    'STRIPE_PUBLIC_KEY',
    'pk_test_51SUWHsK8fYvT5V5ZvnbkBV1Lc5jU1SWw1WojQjgct3dedaoUVr6N0tk5iFQmvcBk4MoOYb6TCfRSjAfJ40j9gAaV00ogvGeuyM'  # Replace with your Stripe test publishable key
)

# ------------------------------
#   FRONTEND URL
# ------------------------------
FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://127.0.0.1:8000')

