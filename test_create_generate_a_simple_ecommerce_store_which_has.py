import pytest
from create_generate_a_simple_ecommerce_store_which_has import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_dashboard(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Product A' in response.data
    assert b'Product B' in response.data
    assert b'Product C' in response.data
    assert b'Total Sales:' in response.data
