from demo.settings.base import *  # noqa: F401,F403,F405

DEBUG = True

INSTALLED_APPS += [
    'storages',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}

# AWS configurations
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = env("AWS_DEFAULT_REGION")

# S3 STATIC SETTINGS
STATICFILES_LOCATION = "static"
MEDIAFILES_LOCATION = "media"

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = "{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

STATICFILES_STORAGE = "demo.storage_backends.StaticStorage"
DEFAULT_FILE_STORAGE = "demo.storage_backends.MediaStorage"
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)