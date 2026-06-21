# This file serves to test the ecommerce application.
import pytest
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product

# Fixture for creating a test client for the Flask app.
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'E-commerce Dashboard' in response.data


def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 10})
    assert response.status_code == 302  # Should redirect
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 10


def test_record_sale(client):
    client.post('/add_product', data={'name': 'Test Sale Product', 'stock': 10})
    product = Product.query.filter_by(name='Test Sale Product').first()
    assert product is not None
    response = client.post('/record_sale', data={'product_id': product.id, 'quantity': 3})
    assert response.status_code == 302  # Should redirect
    updated_product = Product.query.get(product.id)
    assert updated_product.sales == 3



@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'E-commerce Dashboard' in response.data


def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 10})
    assert response.status_code == 302  # Should redirect
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 10


def test_record_sale(client):
    client.post('/add_product', data={'name': 'Test Sale Product', 'stock': 10})
    product = Product.query.filter_by(name='Test Sale Product').first()
    assert product is not None
    response = client.post('/record_sale', data={'product_id': product.id, 'quantity': 3})
    assert response.status_code == 302  # Should redirect
    updated_product = Product.query.get(product.id)
    assert updated_product.sales == 3
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client

from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product

from flask import Flask
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Products' in response.data


def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 10})
    assert response.status_code == 302  # Should redirect
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 10


def test_record_sale(client):
    # Setup: add a product first
    client.post('/add_product', data={'name': 'Test Sale Product', 'stock': 10})
    product = Product.query.filter_by(name='Test Sale Product').first()
    assert product is not None

    # Record a sale
    response = client.post('/record_sale', data={'product_id': product.id, 'quantity': 3})
    assert response.status_code == 302  # Should redirect
    updated_product = Product.query.get(product.id)
    assert updated_product.sales == 3


# This fixture should only be defined once. It creates a test client for the app.

def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 50})
    assert response.status_code == 302  # Redirect to index
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 50
    assert product.sales == 0
    assert product.stock == 50
def test_record_sale(client):
    client.post('/add_product', data={'name': 'Test Product', 'stock': 100})
    response = client.post('/record_sale/1', data={'quantity': 1})
    assert response.status_code == 302  # Redirect to index
    product = Product.query.get(1)
    assert product.stock == 99
    assert product.sales == 1

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture()
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Dashboard' in response.data  # Ensure 'Dashboard' is in the index page
def test_record_sale_failure(client):
    client.post('/add_product', data={'name': 'Test Product', 'stock': 2})
    client.post('/add_product', data={'name': 'Test Product', 'stock': 2})  # Add a product for testing
    response = client.post('/record_sale', data={'product_id': 1, 'quantity': 5})
    assert response.status_code == 302  # Check if it redirects even if sale wasn't successful
    assert app.products[0]['stock'] == 2  # Stock should not have changed
@pytest.fixture
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
@pytest.fixture
def test_record_sale(client):
    client.post('/add_product', data={'product_name': 'Test Product', 'stock_level': 10})
    response = client.post('/record_sale', data={'product_name': 'Test Product', 'quantity_sold': 5})
    assert response.status_code == 302  # Redirects back to index
    response = client.get('/'); assert 'Test Product' in response.get_data(as_text=True)
