from flask import Blueprint, request, jsonify
import requests
import copy
from bs4 import BeautifulSoup

from iSearchWsApi.blueprints import mockdata

api = Blueprint("api", __name__, url_prefix="/api")

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


@api.route("/google")
def googleApi():
    # from
    # https://automatetheboringstuff.com/chapter11/
    q = request.args.get("q")  # not requests
    mock = request.args.get("mock")  # not requests
    blocked = request.args.get("blocked")  # not requests
    print("q = " + q)
    if mock:
        print("mock = " + mock)
    if blocked:
        print("blocked = " + blocked)
        return '{"message": "ERROR: we have been BLOCKED"}'

    print("Googling...")  # display text while downloading the Google page

    if mock:
        if q == "kittens":
            return jsonify(mockdata.mockDataKittens)
        elif q == "cats":
            return jsonify(mockdata.mockDataCats)
        elif q == "cars":
            return jsonify(mockdata.mockDataCars)
        else:
            return '{"message": "mocked"}'
    # if (mock == 0):
    if q == "500":
        # 503 Server Error: Service Unavailable for url:
        #   https://www.google.com/sorry/index?continue=
        #   https://www.google.com/search%3Fq%3Dblocked%26oq%3D
        #   blocked%26hl%3Den%26gl%3Dus%26sourceid%3D
        #   chrome%26ie%3DUTF-8&hl=en&
        #   q=EgQyTvRhGNG5mOIFIhkA8aeDS7SXjlGndA50dtMVc_Y3HaUq6drtMgFy
        # res = requests.get('https://google.com/search?q=internal%20error&q=EgQyTvRhGN&usasourc=chrome&ved=xUTF-8')
        res = requests.get(
            "https://www.google.com/sorry/index?continue="
            "https://www.google.com/search%3Fq%3Dblocked%26oq%3D"
            "blocked%26hl%3Den%26gl%3Dus%26sourceid%3Dchrome%26ie%3DUTF-8&hl=en"
        )
    elif q == "400":
        res = requests.get(
            "https://google.com/sorry?q=&oq=&hl=en&gl=us&sourceid=chrome&ie=UTF-8"
        )
    else:
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
        print("Client ERROR Returned " + str(res.status_code))
        # return(res.text)
        return '{"message": "Client ERROR: ' + str(res.status_code) + '"}'

    if (res.status_code >= 500) and (res.status_code < 600):
        print("Server ERROR Returned " + str(res.status_code))
        if "blocked" in res.text:
            print("we've been blocked")
            return '{"message": "ERROR: we have been BLOCKED"}'
        # return(res.text)
        return '{"message": "Server ERROR: ' + str(res.status_code) + '"}'

    #   print some html reponse information
    if verbose > 0:
        print("status = " + str(res.status_code))
        print(res.headers.get("content-type", "unknown"))

    # Retrieve top search result links.
    soup = BeautifulSoup(res.text, "html.parser")
    #   print("soup ="+soup)
    #   print(soup)

    # Open a browser tab for each result.
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
    total_results = result_count

    if verbose > 3:
        print("\n\ntotal_results")
        print(total_results)

    # then gen JSON
    # data1 = data # empty struct
    # data1 = data[:] # empty struct
    # https://stackoverflow.com/questions/5105517/deep-copy-of-a-dict-in-python
    data1 = copy.deepcopy(data)  # empty struct
    if verbose > 6:
        print("post-copy, pre-fill data1: ")
        print(data1)

    data1["search_parameters"]["q"] = q
    data1["search_information"]["total_results"] = total_results[0]
    # "organic_results": []
    for x in range(len(titleElems)):
        position = x
        title = titleElems[x].text
        # print("title = "+title+"\n")
        link = titleElems[x]["href"][7:]  # remove /url?q=
        # print("link = "+link+"\n")
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
        if len(abstractElems) > x:
            snippet = abstractElems[x].text
        else:
            snippet = ""
        data1["organic_results"].append(
            {"position": position, "title": title, "link": link, "snippet": snippet}
        )

        # "related_questions": []

        # "related_searches": [ ]
        if relatedSearches:
            for x in range(len(relatedSearches)):
                query = relatedSearches[x].text
                link = relatedSearches[x]["href"]
                data1["related_searches"].append({"query": query, "link": link})

        if verbose > 6:
            print("returned data1 out:")
            print(data1)

    return jsonify(data1)
    # return ('{"message": "ERROR: not yet supported"}')


@api.route("/ddg")
def ddgApi():
    return '{"message": "ERROR: not yet supported"}'


@api.route("/bing")
def bingApi():
    return '{"message": "ERROR: not yet supported"}'


@api.route("/multi")
# multiple engines
def multipleEnginesApi():
    return '{"message": "ERROR: not yet supported"}'
