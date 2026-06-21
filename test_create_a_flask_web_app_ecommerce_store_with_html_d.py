import pytest
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product, Sale
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_dashboard(client):
    response = client.get('/')
    assert b'Dashboard' in response.data

def test_add_product(client):
    response = client.post('/add_product', data={
        'name': 'Test Product',
        'stock': 10,
        'price': 99.99
    })
    assert response.status_code == 302  # Redirect
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 10
    assert product.price == 99.99

def test_record_sale(client):
    client.post('/add_product', data={
        'name': 'Test Product2',
        'stock': 10,
        'price': 20.00
    })
    product = Product.query.filter_by(name='Test Product2').first()
    response = client.post('/record_sale', data={
        'product_id': product.id,
        'quantity': 2
    })
    assert response.status_code == 302  # Redirect
    sale = Sale.query.filter_by(product_id=product.id).first()
    assert sale is not None
    assert sale.quantity == 2
    assert sale.total_price == 40.00
    assert product.stock == 8  # Stock should decrease