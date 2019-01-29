from flask import Flask
#from celery import Celery

from iSearchWsApi.blueprints.page.views import page
from iSearchWsApi.blueprints.api.raw import raw
from iSearchWsApi.blueprints.api.search import search
from iSearchWsApi.blueprints.api.api import api
#from iSearchWsApi.extensions import debug_toolbar, csrf
#from iSearchWsApi.extensions import csrf

def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

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
#    csrf.init_app(app)

    return None

# only used if: python iSearchWsApi/app.py
if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)

