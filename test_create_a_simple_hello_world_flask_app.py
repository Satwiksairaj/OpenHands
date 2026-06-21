import pytest
from create_a_simple_hello_world_flask_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

