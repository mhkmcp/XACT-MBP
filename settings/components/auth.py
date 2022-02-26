from decouple import config
from .common import PRODUCTION


# SECURITY WARNING: keep the secret key used in production secret!
if PRODUCTION:
    SECRET_KEY = config('SECRET_KEY')
else:
    SECRET_KEY = config('SECRET_KEY', default='kwqf$5qd*gg8mefrn5lcc6kz8_yo%knfb2g9z8rtup=&+!g*jl')


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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