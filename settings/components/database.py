import os
from pathlib import Path

from decouple import config
# from xact_dashboard.settings.paths import BASE_DIR
from ..paths import BASE_DIR


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}