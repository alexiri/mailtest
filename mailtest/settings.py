import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-dev-only-change-me")
DEBUG = os.environ.get("DEBUG", "true").lower() in {"1", "true", "yes", "on"}
ALLOWED_HOSTS = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "*").split(",") if h.strip()]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "post_office",
    "django_ses",
    "mailer",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mailtest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "mailtest.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# If served behind HTTPS and a custom domain, set CSRF_TRUSTED_ORIGINS.
# Example: CSRF_TRUSTED_ORIGINS=https://astra.almalinux.org
CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# Send email via django-post-office and SES by default.
EMAIL_BACKEND = "post_office.EmailBackend"

POST_OFFICE = {
    "DEFAULT_PRIORITY": "now",
    "MAX_RETRIES": 2,
    "RETRY_INTERVAL": 300,
    "BACKENDS": {
        "default": "django_ses.SESBackend",
        "ses": "django_ses.SESBackend",
        "smtp": "django.core.mail.backends.smtp.EmailBackend",
    },
}

# AWS SES (required for sending)
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", "us-east-1")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT", f"email.{AWS_SES_REGION_NAME}.amazonaws.com")
AWS_SES_CONFIGURATION_SET = os.environ.get("AWS_SES_CONFIGURATION_SET") or None

# SNS events webhooks (bounces, complaints, deliveries, opens, clicks)
AWS_SES_VERIFY_EVENT_SIGNATURES = os.environ.get("AWS_SES_VERIFY_EVENT_SIGNATURES", "false").lower() in {"1", "true", "yes", "on"}
AWS_SES_USE_BLACKLIST = os.environ.get("AWS_SES_USE_BLACKLIST", "true").lower() in {"1", "true", "yes", "on"}
AWS_SES_ADD_BOUNCE_TO_BLACKLIST = os.environ.get("AWS_SES_ADD_BOUNCE_TO_BLACKLIST", "true").lower() in {"1", "true", "yes", "on"}
AWS_SES_ADD_COMPLAINT_TO_BLACKLIST = os.environ.get("AWS_SES_ADD_COMPLAINT_TO_BLACKLIST", "true").lower() in {"1", "true", "yes", "on"}

# Jazzmin minimal tweaks
JAZZMIN_SETTINGS = {
    "site_title": "Mailtest Admin",
    "site_header": "Mailtest",
}
