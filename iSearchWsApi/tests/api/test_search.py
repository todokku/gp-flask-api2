import pytest
from flask import url_for
import json
from iSearchWsApi.blueprints import mockdata

#print(mockdata.mockDataKittens)
#print(mockdata.mockDataCats)
#print(mockdata.mockDataCars)

class TestSearch(object):
    def test_google_api(self, client):
        """ google api should respond with a success 200. """
        response = client.get(url_for('search.google')+'?q=test')
        assert response.status_code == 200

    def test_ddg_api(self, client):
        """ ddg api should respond with a success 200. """
        response = client.get(url_for('search.ddg'))
        assert response.status_code == 200

    def test_bing_api(self, client):
        """ bing api should respond with a success 200. """
        response = client.get(url_for('search.bing'))
        assert response.status_code == 200

    def test_multi_api(self, client):
        """ multi-engine api should respond with a success 200. """
        response = client.get(url_for('search.multipleEngines'))
        assert response.status_code == 200

# --- Google search API testing
@pytest.mark.parametrize(('query', 'message', 'count'), (
    ('cats', b'{"message": "ERROR: not yet supported"}', 10),
    ('cars', b'{"message": "ERROR: not yet supported"}', 13),
    ('kittens', b'{"message": "ERROR: not yet supported"}', 10),
    #('blocked', {"message": "blocked"}, 0),
))

def test_google_search_live(client, query, message, count):
    response = client.get(
        '/search/google?q='+query
    )

    dic = json.loads(response.data)
    #assert query in dic.search_parameters.q
    assert query in dic['search_parameters']['q']
    #assert message in response.data.search_parameters.q
    assert count == len(dic['organic_results'])


@pytest.mark.parametrize(('query', 'message'), (
    #('cats', '{"message": "mocked"}'),
    ('cats', mockdata.mockDataCats),
    #('cars', '{"message": "mocked"}'),
    ('cars', mockdata.mockDataCars),
    #('kittens', b'{"message": "mocked"}'),
    ('kittens', mockdata.mockDataKittens),
    ('other', {"message": "mocked"}),
))

def test_google_search_mock(client, query, message):
    response = client.get(
        '/search/google?q='+query+'&mock=1'
    )

    mockResponse = json.loads(response.data.decode('utf-8'))
    #dicMessage = json.load(message)

    #assert message in response.data
    #assert dicMessage == response.data
    #assert message in mockResponse
    assert message == mockResponse
    #assert message == response.data

def test_google_search_blocked(client):
    response = client.get(
        '/search/google?q='+'blocked'+'&blocked=1'
    )

    mockResponse = json.loads(response.data.decode('utf-8'))
    #assert 'BLOCKED' in mockResponse
    assert {'message': 'ERROR: we have been BLOCKED'} == mockResponse


# --- DDG search API testing
@pytest.mark.parametrize(('query', 'message'), (
    ('cats', b'{"message": "ERROR: not yet supported"}'),
    ('cars', b'{"message": "ERROR: not yet supported"}'),
    ('kittens', b'{"message": "ERROR: not yet supported"}'),
))

def test_ddg_search_live(client, query, message):
    response = client.get(
        '/search/ddg?q='+query
    )
    assert message in response.data



# --- Bing search API testing
@pytest.mark.parametrize(('query', 'message'), (
    ('cats', b'{"message": "ERROR: not yet supported"}'),
    ('cars', b'{"message": "ERROR: not yet supported"}'),
    ('kittens', b'{"message": "ERROR: not yet supported"}'),
))

def test_bing_search_live(client, query, message):
    response = client.get(
        '/search/bing?q='+query
    )
    assert message in response.data



# --- Multi search API testing
@pytest.mark.parametrize(('query', 'message'), (
    ('cats', b'{"message": "ERROR: not yet supported"}'),
    ('cars', b'{"message": "ERROR: not yet supported"}'),
    ('kittens', b'{"message": "ERROR: not yet supported"}'),
))

def test_multi_search_live(client, query, message):
    response = client.get(
        '/search/multi?q='+query
    )
    assert message in response.data

