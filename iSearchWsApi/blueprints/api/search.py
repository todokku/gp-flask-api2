from flask import Blueprint, request
import requests
from bs4 import BeautifulSoup

from iSearchWsApi.blueprints import mockdata

search = Blueprint("search", __name__, url_prefix="/search")

verbose = 9  # all the debug prints

# headers to use in Get
headers_Get = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# use SerpAPI format for easy digest
data = {
    "search_metadata": {},
    "search_parameters": {},
    "search_information": {},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [],
    "related_searches": [],
    "pagination": {},
}


@search.route("/google")
def google():
    # from
    # https://automatetheboringstuff.com/chapter11/
    q = request.args.get("q")  # not requests
    mock = request.args.get("mock")  # not requests
    blocked = request.args.get("blocked")  # not requests
    print("q = " + str(q))
    if mock:
        print("mock = " + str(mock))
    if blocked:
        print("blocked = " + str(blocked))
        return '{"message": "ERROR: we have been BLOCKED"}'

    print("Googling...")  # display text while downloading the Google page

    # FIXME should return html from parseJsonResults() and be sent GS html data
    if mock:
        if q == "kittens":
            # return(jsonify(mockdata.mockDataKittens))
            # return(parseJsonResults(json.loads(mockdata.mockDataKittens)))
            # return(parseJsonResults(mockdata.mockDataKittensHtml, q))
            return mockdata.mockDataKittensHtml
        elif q == "cats":
            # return(jsonify(mockdata.mockDataCats))
            return mockdata.mockDataCatsHtml
        elif q == "cars":
            # return(jsonify(mockdata.mockDataCars))
            return mockdata.mockDataCarsHtml
        else:
            # return ('{"message": "mocked"}')
            return mockdata.mockDataHtml
    # if (mock == 0):
    # else:
    # res = requests.get('http://google.com/search?q=' + q)
    res = requests.get(
        "https://google.com/search?q="
        + q
        + "&oq="
        + q
        + "&hl=en&gl=us&sourceid=chrome&ie=UTF-8"
    )
    # res.raise_for_status() # not in production
    if (res.status_code >= 400) and (res.status_code < 500):
        """
      return('<html><head></head><body><h2>Client ERROR Returned '+str(res.status_code)+
        '</h2><p>'+res.text+'<br></body></html>')
      """
        print("Client ERROR Returned " + str(res.status_code))
        return res.text

    if (res.status_code >= 500) and (res.status_code < 600):
        """
      return('<html><head></head><body><h2>Server Error Returned '+str(res.status_code)+
        '</h2><p>'+res.text+'<br></body></html>')
      """
        print("Server ERROR Returned " + str(res.status_code))
        return res.text

    #   print some html reponse information
    if verbose > 0:
        print("status = " + str(res.status_code))
        print(res.headers.get("content-type", "unknown"))
    return parseJsonResults(res.text, q)


def parseJsonResults(dicResults, q):

    # Retrieve top search result links.
    # soup = BeautifulSoup(res.text,"html.parser")
    soup = BeautifulSoup(dicResults, "html.parser")
    #   print("soup ="+soup)
    #   print(soup)

    # Open a browser tab for each result.
    result_count = [0]

    linkElems = soup.select(".r a")  # osearch links and titles
    abstractElems = soup.select(".st")  # osearch snippets
    relatedSearches = soup.select(".aw5cc a")
    #   relatedQuestions = soup.select('.st span')
    for resultStats in soup.find_all("div", "sd"):
        result_count = resultStats.contents
    #     print("s")

    #   for titleElems in soup.find_all("div", "r"):
    titleElems = soup.select(".r a")
    for x in range(len(titleElems)):
        title = titleElems[x].text
        print("title = " + title + "\n")
        link = titleElems[x]["href"]
        print("link = " + link + "\n")

    if verbose > 3:
        print("\n\nlinkElems")
        print(*linkElems, sep="\n")

        print("\n\nabstractElems")
        print(*abstractElems, sep="\n")

    if relatedSearches:
        if verbose > 3:
            print("\n\nrelatedSearches")
            print(*relatedSearches, sep="\n")

    #    print(*resultStats, sep = "\n")
    #    total_results = int(resultStats[0])
    total_results = result_count[0]

    if verbose > 3:
        print("\n\ntotal_results")
        print(total_results)

    # then return HTML
    html = "<!DOCTYPE doctype html><head></head><body>"
    #    for x in range(len(resultStats)):
    #        html=html+"<p>"+str(resultStats[x])+"<br>"
    # for x in range(len(total_results)):
    html = html + "<p> Total Results: " + str(total_results) + "<br>"
    if verbose > 5:
        print("<p>" + str(total_results) + "<br>")
    html = html + "<h2>Related Searches</h2>"
    for x in range(len(relatedSearches)):
        html = html + str(relatedSearches[x]) + "<br><br>"
        if verbose > 5:
            print(str(relatedSearches[x]) + "<br><br>")
    html = html + "<h2>Related Questions</h2>"

    html = html + "<h2>Organic Results</h2>"
    for x in range(len(linkElems)):
        html = html + str(linkElems[x]) + "<br>"
        if verbose > 5:
            print("linkElems=" + str(len(linkElems)) + " x=" + str(x) + "\n")
        # can have link without snippet?
        if verbose > 5:
            print(
                "linkElems="
                + str(len(linkElems))
                + " abstractElems="
                + str(len(abstractElems))
                + " x="
                + str(x)
                + "\n"
            )
        if (len(abstractElems)) > x:
            html = html + str(abstractElems[x]) + "<br><br>"

    html = html + "</body></html>"

    # then gen JSON

    # json1 = '{ "search_parameters": { "q": "' + q
    # json2 = '"}, "search_information": { "total_results": ' + str(total_results)
    # json3 = '},"related_questions": [],"organic_results": ['
    #
    #    position?
    #    title
    #    link
    #    snippet
    #    date - optional
    #
    # json4 = '],  "related_searches": [ '
    #
    #    query
    #    link
    #
    # json5 = "]}"

    print("html returned:")
    print(html)
    return html  # show URLs
    # return ('{"message": "ERROR: not yet supported"}')


@search.route("/ddg")
def ddg():
    return '{"message": "ERROR: not yet supported"}'


@search.route("/bing")
def bing():
    return '{"message": "ERROR: not yet supported"}'


@search.route("/multi")
# multiple engines
def multipleEngines():
    return '{"message": "ERROR: not yet supported"}'


@search.route("/serpapi")
def serpApi():
    # from
    # https://automatetheboringstuff.com/chapter11/
    q = request.args.get("q")  # not requests
    mock = request.args.get("mock")  # not requests
    blocked = request.args.get("blocked")  # not requests
    print("q = " + str(q))
    if mock:
        print("mock = " + str(mock))
    if blocked:
        print("blocked = " + str(blocked))
        return '{"message": "ERROR: we have been BLOCKED"}'

    print("SerpApi-ing...")  # display text while downloading the Google page

    # FIXME should return html from parseJsonResults() and be sent GS html data
    if mock:
        if q == "kittens":
            # return(jsonify(mockdata.mockDataKittens))
            # return(parseJsonResults(json.loads(mockdata.mockDataKittens)))
            # return(parseJsonResults(mockdata.mockDataKittensHtml, q))
            return mockdata.mockDataKittensHtml
        elif q == "cats":
            # return(jsonify(mockdata.mockDataCats))
            return mockdata.mockDataCatsHtml
        elif q == "cars":
            # return(jsonify(mockdata.mockDataCars))
            return mockdata.mockDataCarsHtml
        else:
            # return ('{"message": "mocked"}')
            return mockdata.mockDataHtml
    # if (mock == 0):
    # else:
    # res = requests.get('http://google.com/search?q=' + q)
    # $ curl --get https://serpapi.com/search \
    # -d q="Coffee" \
    # -d hl="en" \
    # -d gl="us" \
    # -d google_domain="google.com" \
    # -d api_key="194a4b22789db07b2e0957b87615316d0f0045918a9dd4b5f8e8162b4020da43"
    res = requests.get(
        "https://serpapi.com/search.json?q="
        + q
        + "&hl=en&gl=us&google_domain=google.com"
        + "&api_key=194a4b22789db07b2e0957b87615316d0f0045918a9dd4b5f8e8162b4020da43"
    )
    # print(res)
    # print(*res)

    # res.raise_for_status() # not in production
    if (res.status_code >= 400) and (res.status_code < 500):
        """
      return('<html><head></head><body><h2>Client ERROR Returned '+str(res.status_code)+
        '</h2><p>'+res.text+'<br></body></html>')
      """
        print("Client ERROR Returned " + str(res.status_code))
        return res.text

    if (res.status_code >= 500) and (res.status_code < 600):
        """
      return('<html><head></head><body><h2>Server Error Returned '+str(res.status_code)+
        '</h2><p>'+res.text+'<br></body></html>')
      """
        print("Server ERROR Returned " + str(res.status_code))
        return res.text

    data = res.json()

    #   print some html reponse information
    if verbose > 0:
        print("status = " + str(res.status_code))
        print(res.headers.get("content-type", "unknown"))

        total_results = data["search_information"]["total_results"]
        relatedSearches = data["related_searches"]
        linkElems = data["organic_results"]

    # then return HTML
    html = "<!DOCTYPE doctype html><head></head><body>"
    #    for x in range(len(resultStats)):
    #        html=html+"<p>"+str(resultStats[x])+"<br>"
    # for x in range(len(total_results)):
    html = html + "<p> Total Results: " + str(total_results) + "<br>"
    if verbose > 5:
        print("<p>" + str(total_results) + "<br>")
    html = html + "<h2>Related Searches</h2>"
    for x in range(len(relatedSearches)):
        html = html + str(relatedSearches[x]["query"]) + "<br><br>"
        if verbose > 5:
            print(str(relatedSearches[x]) + "<br><br>")
    html = html + "<h2>Related Questions</h2>"

    html = html + "<h2>Organic Results</h2>"
    for x in range(len(linkElems)):
        html = html + str(linkElems[x]["title"]) + "<br>"
        html = html + str(linkElems[x]["link"]) + "<br>"
        html = html + str(linkElems[x]["snippet"]) + "<br><br>"
        if verbose > 5:
            print("linkElems=" + str(len(linkElems)) + " x=" + str(x) + "\n")
    html = html + "</body></html>"

    # then gen JSON

    # json1 = '{ "search_parameters": { "q": "' + q
    # json2 = '"}, "search_information": { "total_results": ' + str(total_results)
    # json3 = '},"related_questions": [],"organic_results": ['
    #
    #    position?
    #    title
    #    link
    #    snippet
    #    date - optional
    #
    # json4 = '],  "related_searches": [ '
    #
    #    query
    #    link
    #
    # json5 = "]}"

    print("html returned:")
    print(html)
    return html  # show URLs
    # return ('{"message": "ERROR: not yet supported"}')
