import requests, sys, webbrowser, copy, json
from flask import Blueprint, request, jsonify
from iSearchWsApi.blueprints import mockdata

raw = Blueprint('raw', __name__, url_prefix='/raw')

verbose = 9 # all the debug prints

# headers to use in Get
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

@raw.route('/google', methods=['GET'])
def googleRaw():
    # from
    # https://automatetheboringstuff.com/chapter11/
    q = request.args.get('q') # not requests
    mock = request.args.get('mock') # not requests
    print("q = "+q)
    if (mock):
      print("mock = "+mock)
    print('Googling...') # display text while downloading the Google page

    if (mock):
      if (q == 'kittens'):
        return(jsonify(mockdata.mockDataKittensHtml))
        #return (mockData)
      elif (q == 'cats'):
        return(jsonify(mockdata.mockDataCatsHtml))
      elif (q == 'cars'):
        return(jsonify(mockdata.mockDataCarsHtml))
      else:
        return ('{"message": "mocked"}')
    #if (mock == 0):
    res = requests.get('https://google.com/search?q=' +q+ '&oq='+q+'&hl=en&gl=us&sourceid=chrome&ie=UTF-8')
    res.raise_for_status()

#   print some html reponse information
    if (verbose > 0):
      print("status = "+str(res.status_code))
      if "blocked" in res.text:
        print( "we've been blocked")
        return ('{"message": "ERROR: we have been BLOCKED"}')
      print (res.headers.get("content-type", "unknown"))

    return (res.text) # show html page

@raw.route('/ddg')
def ddgRaw():
    return ('{"message": "ERROR: not yet supported"}')

@raw.route('/bing')
def bingRaw():
    return ('{"message": "ERROR: not yet supported"}')

@raw.route('/multi')
# multiple engines
def multipleEnginesRaw():
    return ('{"message": "ERROR: not yet supported"}')

