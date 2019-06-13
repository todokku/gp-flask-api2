from flask import Flask
from flask_cors import CORS

# from celery import Celery

## Rollbar init code. You'll need the following to use Rollbar with Flask.
## This requires the 'blinker' package to be installed

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

from iSearchWsApi.blueprints.page.views import page
from iSearchWsApi.blueprints.api.raw import raw
from iSearchWsApi.blueprints.api.search import search
from iSearchWsApi.blueprints.api.api import api

# from iSearchWsApi.extensions import debug_toolbar, csrf
from iSearchWsApi.extensions import csrf

# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/
# def create_app(settings_override=None):
def create_app(config_pyfile=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    # add global CORS support
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)
    # only support config/settings files for config
    # app.config.from_object('config.settings')
    app.config.from_object(config_pyfile)
    # app.config.from_pyfile('settings.py', silent=True)
    # app.config.from_pyfile(config_pyfile, silent=True)
    # app.config.from_pyfile(config_pyfile, silent=False)

    # if settings_override:
    #    app.config.update(settings_override)

    # now log config being used
    app.logger.info("Debug status is: " + str(app.config["DEBUG"]))
    app.logger.info("Testing status is: " + str(app.config["TESTING"]))
    app.logger.info("Development status is: " + str(app.config["DEVELOPMENT"]))
    app.logger.info("Server Name is: " + str(app.config["SERVER_NAME"]))

    # @app.before_first_request
    # def init_rollbar():
    # init rollbar module
    rollbar.init(
        # access token for the app
        str(app.config["ROLLBAR_TOKEN"]),
        # environment name
        str(app.config["ROLLBAR_ENVIRONMENT"]),
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False,
    )

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
    rollbar.report_message("Starting app for flask-api2", "info")

    app.register_blueprint(page)
    app.register_blueprint(raw)
    app.register_blueprint(search)
    app.register_blueprint(api)
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    #    debug_toolbar.init_app(app)
    #    mail.init_app(app)
    csrf.init_app(app)

    return None


# only used if: python iSearchWsApi/app.py
if __name__ == "__main__":
    app = create_app("config.settings")
    app.run(debug=True)
