# run this with gunicorn:
#  gunicorn 'iSearchWsApi.wsgi'
#
# from
# https://stackoverflow.com/questions/25319690/how-do-i-run-a-flask-app-in-gunicorn-if-i-used-the-application-factory-pattern
#

from iSearchWsApi.app import create_app

application = create_app("config.settings_production")

application.run()
