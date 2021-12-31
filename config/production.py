from .settings import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = config('pk_test_51KCidHH6jow4CrsuQQHRGYXKxW1jjXRuIhbiLpCQCTcp3k4UGy0tzXq8gPjtnDvDmphmGUYuVswHRwTWWrF7jUQ800VbuzxvFJ')
STRIPE_SECRET_KEY = config('sk_test_51KCidHH6jow4Crsu1Gu7f49lc60nzwRVQDLadXexlb4kg9ZqKufbqQhpoiKKzTlQkyBpAYI89StcpmO91NZxDMU500drZDPsTD')