import pytest
from create_a_flask_web_app_ecommerce_store_with_html_d import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client

# Test index route
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

# Test adding a product
def test_add_product(client):
    response = client.post('/add_product', data={'product_name': 'Test Product', 'stock_level': 10})
    assert response.status_code == 302
    assert b'Test Product' in client.get('/').data  # Check product exists in dashboard

# Test recording a sale
def test_record_sale(client):
    # First add a product
    client.post('/add_product', data={'product_name': 'Test Product', 'stock_level': 10})
    response = client.post('/record_sale', data={'product_name': 'Test Product', 'quantity': 3})
    assert response.status_code == 302
    # Check sales data
    assert b'Test Product' in client.get('/').data