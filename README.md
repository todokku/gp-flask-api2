# gp-flask-api2

## iSearch Web Scraper & API v2.X

[![License](https://img.shields.io/badge/license-COMMERCIAL-red.svg?style=flat-square)](https://github.com/mkobar/gp-flask-api2/blob/master/LICENSE.md)
![GitHub release](https://img.shields.io/github/release/mkobar/gp-flask-api2.svg)
![Code Style](https://img.shields.io/badge/code_style-Black-brightgreen.svg)
![Linted](https://img.shields.io/badge/linted-Flake8-orange.svg)
[![Known Vulnerabilities](https://snyk.io/test/github/mkobar/gp-flask-api2/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/mkobar/gp-flask-api2?targetFile=requirements.txt)
![Security Scanner](https://img.shields.io/badge/security_scanner-Bandit-blue.svg)
![Requires.io](https://img.shields.io/requires/github/mkobar/gp-flask-api2.svg)
![Website](https://img.shields.io/website-up-down-green-red/https/gp-api2.herokuapp.com.svg)

### Google Proxy Flask API using Python, Response and BeautifulSoup

I originally tried to "port" Googler to an API but found it much easier to do the web scraping myself.  Still need to add a lot of functionality (see ToDo list below).

This proxy also displays web and raw web output (for debug)

with Flask, Redis, and Docker.

- Using Docker to "Dockerize" a multi-service Flask app
- Flask blueprints
- Testing and analyzing your code base (both mocked and live)
- Creating a full blown user management system
- Creating a custom admin dashboard
- Logging, middleware and error handling
- Responding with JSON from Flask and creating API requests

## Python Dev setup

### create VirtualEnv

```
mkvirtualenv api2
setprojectdir .
pip install -r requirements.txt
```

### activate VirtualEnv (api2)/workon api2

```
C:\Users\x\Documents\GitHub\gp-flask-api2>workon api2
```

### deactivate

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>deactivate
```

### run the Flask app

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>python iSearchWsApi/app.py
```

### Unit and API testing (including live and mock API testing)

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>pytest -v iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --usesfixture live iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --tb=no --usesfixture live iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --usesfixture mock iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --usesfixture live iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --tb=no --usesfixture live iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --tb=no --usesfixture mock iSearchWsApi
(api2) C:\GitHub\gp-flask-api2>pytest -v --usesfixture live iSearchWsApi/tests/api/test_search.py
(api2) C:\GitHub\gp-flask-api2>pytest -v --tb=no --usesfixture live iSearchWsApi/tests/api/test_search.py
(api2) C:\GitHub\gp-flask-api2>pytest -v --usesfixture mock iSearchWsApi/tests/api/test_search.py
```

### Unit and API testing coverage

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>pytest --cov=iSearchWsApi iSearchWsApi
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>coverage html
```

Then browse to htmlcov/index.html

## Endpoints to test

Show static web page
http://localhost:5000/

Show response as web page (Raw HTML - what Google returns)
http://localhost:5000/raw/google?q=malpractice

Show response as web page (from parsed response data)
http://localhost:5000/search/google?q=malpractice

Send response as JSON (for API)
http://localhost:5000/api/google?q=malpractice

This can also be done interactivaly with Python on the command line:
```
(hello) C:\Users\x\Documents\GitHub\gp-flask>python

>>> import requests
>>> response = requests.get("http://127.0.0.1:5000/api/google?q=malpractice")
>>> response.json()
```
or with cURL:
```
curl http:///127.0.0.1:5000/api/google?q=malpractice
```

## gunicorn local with CygWin
### virtualenv in CygWin
```
python3 /cygdrive/c/Users/x/AppData/Local/Programs/Python/Python37/Lib/site-packages/virtualenv.py .

source bin/activate

pip install -r requirements.txt

```

```
$ gunicorn 'iSearchWsApi.app:create_app()'
[2019-01-28 14:53:03 -0500] [16856] [INFO] Starting gunicorn 19.9.0
[2019-01-28 14:53:03 -0500] [16856] [INFO] Listening at: http://127.0.0.1:8000 (16856)
[2019-01-28 14:53:03 -0500] [16856] [INFO] Using worker: sync
[2019-01-28 14:53:03 -0500] [15976] [INFO] Booting worker with pid: 15976
/cygdrive/c/Users/dbadmin/Documents/GitHub/gp-flask-api2/lib/python3.6/site-packages/flask/sessions.py:208: UserWarning: "localhost" is not a valid cookie domain, it must contain a ".". Add an entry to your hosts file, for example "localhost.localdomain", and use that instead.
  ' "{rv}.localdomain", and use that instead.'.format(rv=rv)
[2019-01-28 14:54:13 -0500] [16856] [CRITICAL] WORKER TIMEOUT (pid:15976)
[2019-01-28 14:54:13 -0500] [15976] [INFO] Worker exiting (pid: 15976)
[2019-01-28 14:54:13 -0500] [2736] [INFO] Booting worker with pid: 2736
[2019-01-28 14:54:29 -0500] [16856] [INFO] Handling signal: winch
```

--check-config appears to fail

```
$ gunicorn --log-level=DEBUG 'iSearchWsApi.app:create_app("config.settings_production")'
```

```
$ gunicorn --log-level=DEBUG --spew 'iSearchWsApi.app:create_app("config.settings_production")'
```
To test CygWin gunicorn:
```
http://localhost:8000/search/google?q=car%20seats

or

http://localhost:8000/
```

## Flake8 - Linter
```
flake8 iSearchWsApi
```

## Black - reformatter
```
black iSearchWsApi
```

## Bandit - source code security analyzer

Run for all issues for entire project
```
bandit -r iSearchWsApi
```

Show only high severity issues for entire project
```
bandit -r iSearchWsApi -lll
```

Show only high severity issues for entire project and included files with score
```
bandit -r iSearchWsApi -lll -v
```

Show only high severity issues for entire project and included files with score and ignore nosec comment action
```
bandit -r iSearchWsApi -lll -v --ignore-nosec
```

## Advanced Topics (ToDo)

- [ ] Continous Integration Testing
- [x] ~~API Testing~~
- [x] ~~Handling Scraping Errors~~
- [x] ~~Handling Network Errors~~
- [x] ~~Flask8 Linting~~
- [x] ~~Black code formatting~~
- [X] ~~Bandit code security scanning~~

## Cache stuff
- [ ] Cache support (in PostgreSQL)
- [ ] Redis support?

### Scraper stuff
- [ ] Sessions and Cookies
- [ ] Delays and Backing Off
- [ ] Spoofing and Cycling the User Agent
- [ ] Using Proxy Servers
- [ ] Setting Timeouts
- [ ] Use Selenium web driver
- [ ] Use PhantomJS for headless JS support

### Service stuff
- [ ] Authentication
- [ ] Logging

## Links

http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

https://blog.hartleybrody.com/web-scraping-cheat-sheet/

https://realpython.com/vim-and-python-a-match-made-in-heaven/#syntax-checkinghighlighting

https://stackoverflow.com/questions/20035101/why-does-my-javascript-get-a-no-access-control-allow-origin-header-is-present

https://pypi.org/project/bandit/

More here: [Iterative Search](http://iterativesearch.com)

