# -*- coding: utf-8 -*-

# flask core settings
DEBUG = True
TESTING = False
DEVELOPMENT = True

#SERVER_NAME = 'localhost:5000'
#SERVER_NAME = 'localhost.localdomain:5000'
SERVER_NAME = '127.0.0.1:5000'
SECRET_KEY = 'insecurekeyfordev'
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# Flask-WTF settings
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

# flask mongoengine settings
MONGODB_SETTINGS = {
    'DB': 'flaskexample'
}

# Flask-Mail settings
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com'
MAIL_PASSWORD = 'awesomepassword'

# Celery settings
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# project settings
PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
PROJECT_SITE_NAME = u'Flask Example'
PROJECT_SITE_URL = u'http://127.0.0.1:5000'
PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds

