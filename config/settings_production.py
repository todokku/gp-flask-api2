# -*- coding: utf-8 -*-
#from config.settings import *
#from settings import *

# does gunicorn use TESTING and DEVELOPMENT?  It sure looks like it.

# flask core settings
DEBUG = False
TESTING = False

#SERVER_NAME = 'app.isearch.com'
#SECRET_KEY = 'generateastrong128chartoken'

DEVELOPMENT = False

# Flask-WTF settings
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True

MAIL_USERNAME = 'you@realemailaccount.com'
MAIL_PASSWORD = 'thebestpasswordyouevermade'

CELERY_BROKER_URL = 'redis://:amuchmoresecurepassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:amuchmoresecurepassword@redis:6379/0'
