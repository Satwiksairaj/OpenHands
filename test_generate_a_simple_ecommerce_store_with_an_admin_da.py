import pytest
import json
from generate_a_simple_ecommerce_store_with_an_admin_da import admin_dashboard, Product, Order

def test_add_product():
    product = Product("Test Product", 100.0, 5)
    admin_dashboard.add_product(product)
    assert len(admin_dashboard.products) == 1
def test_create_order_successful():
    product = Product("Test Product", 100.0, 5)
    admin_dashboard.add_product(product)
    order = admin_dashboard.create_order("Test Product", 2)
    assert order.quantity == 2
    assert product.stock == 3
def test_create_order_insufficient_stock():
    product = Product("Test Product", 100.0, 1)
    admin_dashboard.add_product(product)
    with pytest.raises(ValueError):
        admin_dashboard.create_order("Test Product", 2)
def test_sales_report():
    product1 = Product("Product 1", 100.0, 5)
    admin_dashboard.add_product(product1)
    admin_dashboard.create_order("Product 1", 1)
    sales_report = admin_dashboard.get_sales_report()
    assert len(sales_report) == 1
    assert sales_report[0]['quantity'] == 1
