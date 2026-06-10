import pytest
from flask import Flask
from create_a_flask_web_app_ecommerce_store_with_html_d import app

def test_sell_product(client):
    response = client.get('/sell_product?product_name=Sample Product')
    assert response.status_code == 200
    assert b'Sell Sample Product' in response.data

def test_record_sale(client):
    response = client.post('/record_sale', data={"product_name": "Sample Product", "quantity": 2})
    assert response.status_code == 302
    assert b'Product not available.' not in response.data