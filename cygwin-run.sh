# runs gunicorn with virualEnv in Cygwin
#
`( source bin/activate; gunicorn -b localhost.localdomain:5000 -t 90 'iSearchWsApi.app:create_app("config.settings_production")' )`

