"""
Tests for Flask E-Commerce Store
"""
import pytest
from create_a_flask_web_app_ecommerce_store_with_dashbo import app, products, sales


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear state before each test
        products.clear()
        sales.clear()
        yield client


def test_home_page(client):
    """Test that home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'E-Commerce Dashboard' in response.data


def test_dashboard_page(client):
    """Test that dashboard page loads successfully."""
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Stock Levels' in response.data


def test_add_product(client):
    """Test adding a new product."""
    response = client.post('/add_product', data={
        'product_name': 'Test Product',
        'stock_level': '10'
    })
    assert response.status_code == 302  # Redirect
    assert products['Test Product'] == 10


def test_record_sale(client):
    """Test recording a sale."""
    # First add a product
    products['Test Product'] = 5
    
    response = client.post('/record_sale', data={
        'product_name': 'Test Product'
    })
    assert response.status_code == 302  # Redirect
    assert products['Test Product'] == 4
    assert 'Test Product' in sales


def test_record_sale_no_stock(client):
    """Test that sale is not recorded when no stock."""
    products['Empty Product'] = 0
    
    response = client.post('/record_sale', data={
        'product_name': 'Empty Product'
    })
    assert response.status_code == 302
    assert products['Empty Product'] == 0
    assert 'Empty Product' not in sales