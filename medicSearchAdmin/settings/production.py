import os
from pathlib import Path
from .settings import *
from dotenv import load_dotenv

DEBUG = False

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))
# secret key
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}