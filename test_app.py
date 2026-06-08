import pytest
from app import app, db
from models import Product, Sale
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

# Test the /sales endpoint
def test_sales_transaction(client):
    # Seed a product
    product = Product(name='Laptop', price=1000.00, stock=10, category='Electronics')
    db.session.add(product)
    db.session.commit()

    # Post a sale
    response = client.post('/sales', data={
        'product_id': product.id,
        'quantity': 2,
        'customer_name': 'John Doe',
        'csrf_token': client.get('/sales').data.split(b'csrf_token" type="hidden" value="')[1].split(b'"')[0].decode() if b'csrf_token" type="hidden" value="' in client.get('/sales').data else ''
    }, follow_redirects=True)

    assert response.status_code == 200
    final_product = Product.query.get(product.id)
    assert final_product.stock == 8
    sale = Sale.query.filter_by(customer_name='John Doe').first()
    assert sale.quantity == 2
    assert sale.product_id == product.id

# Test the /products endpoint
def test_product_creation(client):
    # Add a new product
    response = client.post('/products', data={
        'name': 'Smartphone',
        'price': 500.00,
        'stock': 50,
        'category': 'Electronics',
        'csrf_token': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    product = Product.query.filter_by(name='Smartphone').first()
    assert product.price == 500.00
    assert product.stock == 50

# Test the /api/stats endpoint
def test_api_stats(client):
    # Seed a product
    db.session.add(Product(name='Camera', price=250.00, stock=20, category='Electronics'))
    db.session.commit()

    # Check API response
    response = client.get('/api/stats')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['total_products'] == 1
    assert data['total_products'] > 0
