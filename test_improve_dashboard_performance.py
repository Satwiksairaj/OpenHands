import pytest
from flask import url_for
from improve_dashboard_performance import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_dashboard_data(client):
    response = client.get('/api/dashboard')
    assert response.status_code == 200
    data = response.get_json()
    assert 'widget_1' in data
    assert 'widget_2' in data
    assert isinstance(data['widget_1'], list)
    assert isinstance(data['widget_2'], list) 


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Dashboard' in response.data


# Running tests with:
# pytest test_improve_dashboard_performance.py