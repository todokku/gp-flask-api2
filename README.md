# gp-flask-api2

## iSearch Web Scraper & API v2.0.0

Google Proxy Flask API using Python, Response and BeautifulSoup

I originally tried to "port" Googler to an API but found it much easier to do the web scraping myself.  Still need to add a lot of functionality (see ToDo below).

This proxy also displays web and raw web output (for debug)

with Flask, Redis, and Docker.

- Using Docker to "Dockerize" a multi-service Flask app
- Flask blueprints
- Testing and analyzing your code base
- Creating a full blown user management system
- Creating a custom admin dashboard
- Logging, middleware and error handling
- Responding with JSON from Flask and creating AJAX requests

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
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>python isearch-ws-api/app.py
```

### Unit and API testing (including mock API testing)

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>pytest -v
```

### Unit and API testing coverage

```
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>pytest --cov=isearch-ws-api .
(api2) C:\Users\x\Documents\GitHub\gp-flask-api2>coverage html
```

Then browse to htmlcov/index.html

## Endpoints to test

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

## Advanced Topics (ToDo)

- [ ] CI Testing
- [x] ~~API Testing~~
- [x] ~~Handling Scraping Errors~~
- [ ] Handling Network Errors

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


