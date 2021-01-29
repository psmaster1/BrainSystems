# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_database',
        'USER': 'example',
        'PASSWORD': 'password_example',
        'HOST': 'localhost',
        'PORT': '',
    }
}
