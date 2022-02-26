from decouple import config, Csv


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv())

STATIC_URL = '/static/'

ROOT_URLCONF = 'xact_dashboard.urls'

WSGI_APPLICATION = 'xact_dashboard.wsgi.application'