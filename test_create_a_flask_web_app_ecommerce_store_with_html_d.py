import pytest
from flask import Flask
from create_a_flask_web_app_ecommerce_store_with_html_d import app

@pytest.fixture()
def client() -> FlaskClient:
    app.testing = True
    yield app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Products' in response.data
def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': '10'})
    assert response.status_code == 302  # Redirect to index
    assert b'Test Product' in client.get('/').data
def test_record_sale(client):
    client.post('/add_product', data={'name': 'Test Product', 'stock': '10'})
    response = client.post('/record_sale', data={'product_id': '1', 'quantity': '2'})
    assert response.status_code == 302  # Redirect to index
    product = client.get('/').data
    assert b'Stock: 8' in product  # Stock should be updated
