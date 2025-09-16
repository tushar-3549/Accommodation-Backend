from .base import *  # noqa
import os

DEBUG = False

# Prefer DJANGO_SECRET_KEY; fall back to SECRET_KEY
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or os.environ.get("SECRET_KEY")

# Prefer DJANGO_ALLOWED_HOSTS; else ALLOWED_HOSTS; default '*'
ALLOWED_HOSTS = (os.environ.get("DJANGO_ALLOWED_HOSTS") or os.environ.get("ALLOWED_HOSTS", "*")).split(",")

def _env(name, fallback_names=()):
    """Read env var with optional fallbacks."""
    val = os.environ.get(name)
    if val:
        return val
    for fb in fallback_names:
        v = os.environ.get(fb)
        if v:
            return v
    return None

# Support both DB_* and POSTGRES_* variable styles
DB_NAME = _env("DB_NAME", ("POSTGRES_DB",))
DB_USER = _env("DB_USER", ("POSTGRES_USER",))
DB_PASSWORD = _env("DB_PASSWORD", ("POSTGRES_PASSWORD",))
DB_HOST = _env("DB_HOST", ("POSTGRES_HOST",))
DB_PORT = _env("DB_PORT", ("POSTGRES_PORT",))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT or "5432",
        "OPTIONS": {"sslmode": "require"},  # Render typically needs SSL
        "CONN_MAX_AGE": 60,
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
