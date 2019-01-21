from flask import Flask
#from celery import Celery

from snakeeyes.blueprints.page.views import page
from snakeeyes.blueprints.api.search import api
#from snakeeyes.extensions import debug_toolbar, mail, csrf
from snakeeyes.extensions import csrf

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
    app.register_blueprint(api)
    #app.register_blueprint(contact)
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

# only used if: python snakeeyes/app.py
if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)

