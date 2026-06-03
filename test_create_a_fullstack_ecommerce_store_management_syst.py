import pytest
from fastapi.testclient import TestClient
from create_a_fullstack_ecommerce_store_management_syst import app

client = TestClient(app)

# Test product creation
def test_create_product():
    response = client.post('/products/', json={
        "name": "Test Product",
        "category": "Test Category",
        "price": 10.0,
        "stock": 100,
        "sku": "TP001"
    })
    assert response.status_code == 200
    assert response.json()['name'] == "Test Product"

# Test reading products
def test_read_products():
    response = client.get('/products/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test product update
def test_update_product():
    response = client.post('/products/', json={
        "name": "Test Product",
        "category": "Test Category",
        "price": 10.0,
        "stock": 100,
        "sku": "TP001"
    })
    product_id = response.json()['id']
    response = client.put(f'/products/{product_id}', json={
        "name": "Updated Product",
        "category": "Updated Category",
        "price": 20.0,
        "stock": 50,
        "sku": "TP001"
    })
    assert response.status_code == 200
    assert response.json()['name'] == "Updated Product"

# Test product deletion
