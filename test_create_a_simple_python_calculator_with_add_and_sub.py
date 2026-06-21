import json
import pytest
from create_a_simple_python_calculator_with_add_and_sub import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_add(client):
    response = client.post('/add', json={'a': 3, 'b': 4})
    assert response.status_code == 200
    assert response.json['result'] == 7

def test_add_missing_keys(client):
    response = client.post('/add', json={})
    assert response.status_code == 400
    assert 'error' in response.json

def test_subtract(client):
    response = client.post('/subtract', json={'a': 10, 'b': 4})
    assert response.status_code == 200
    assert response.json['result'] == 6

def test_subtract_missing_keys(client):
    response = client.post('/subtract', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    with app.test_client() as client:
        yield client
