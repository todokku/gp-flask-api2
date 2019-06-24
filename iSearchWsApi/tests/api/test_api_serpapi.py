import pytest
from flask import url_for
import json
from iSearchWsApi.blueprints import mockdata

# print(mockdata.mockDataKittens)
# print(mockdata.mockDataCats)
# print(mockdata.mockDataCars)


class TestApiSerpapi(object):
    def test_serpapi_api(self, client, live):
        """ serpapi api should respond with a success 200. """
        response = client.get(url_for("api.serpApi") + "?q=test")
        assert response.status_code == 200


# --- SerpApi-Google API testing
@pytest.mark.parametrize(
    ("query", "count"),
    (
        ("cats", 6),
        ("cars", 6),
        ("kittens", 6),
        # ('blocked', {"message": "blocked"}, 0),
    ),
)
def test_serpapi_api_live(client, query, count, live):
    response = client.get("/api/serpapi?q=" + query)

    dic = json.loads(response.data)
    # assert query in dic.search_parameters.q
    assert query in dic["search_parameters"]["q"]
    # assert message in response.data.search_parameters.q
    assert count <= len(dic["organic_results"])


@pytest.mark.parametrize(
    ("query", "message", "count"),
    (("cars", b'{"message": "ERROR: not yet supported"}', 13),),
)
def NOtest_serpapi_api_live_oneoff(client, query, message, count, live):
    response = client.get("/api/serpapi?q=" + query)

    dic = json.loads(response.data)
    assert query in dic["search_parameters"]["q"]
    if count != len(dic["organic_results"]):
        assert count - 1 == len(dic["organic_results"])
    else:
        assert count == len(dic["organic_results"])


@pytest.mark.parametrize(
    ("query", "message"),
    (
        # ('cats', '{"message": "mocked"}'),
        ("cats", mockdata.mockDataCats),
        # ('cars', '{"message": "mocked"}'),
        ("cars", mockdata.mockDataCars),
        # ('kittens', b'{"message": "mocked"}'),
        ("kittens", mockdata.mockDataKittens),
        ("other", {"message": "mocked"}),
    ),
)
def test_serpapi_api_mock(client, query, message, mock):
    response = client.get("/api/serpapi?q=" + query + "&mock=1")

    mockResponse = json.loads(response.data.decode("utf-8"))
    # dicMessage = json.load(message)

    # assert message in response.data
    # assert dicMessage == response.data
    # assert message in mockResponse
    assert message == mockResponse
    # assert message == response.data


def test_serpapi_api_blocked(client, mock):
    response = client.get("/api/serpapi?q=" + "blocked" + "&blocked=1")

    mockResponse = json.loads(response.data.decode("utf-8"))
    # assert 'BLOCKED' in mockResponse
    assert {"message": "ERROR: we have been BLOCKED"} == mockResponse
