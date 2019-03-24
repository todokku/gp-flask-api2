# -*- coding: utf-8 -*-
#from config.settings import *

# flask core settings
DEBUG = False
TESTING = True
DEVELOPMENT = True
#SERVER_NAME = '127.0.0.1:5000'    # gives cookie error
SERVER_NAME = 'localhost.dev:5001'    # required for pytest
SECRET_KEY = 'insecurekeyfordev'  # required for csrf

# flask wtf settings
WTF_CSRF_ENABLED = False

# flask mongoengine settings
MONGODB_SETTINGS = {
    'DB': 'flaskexample_test'
}

# password hash method
PROJECT_PASSWORD_HASH_METHOD = 'md5'

# rollbar settings
ROLLBAR_TOKEN = 'e1d42248ad324665a13b6c7c4085b089'
ROLLBAR_ENVIRONMENT = 'testing'
