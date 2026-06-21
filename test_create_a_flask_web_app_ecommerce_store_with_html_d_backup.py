import pytest
from create_a_flask_web_app_ecommerce_store_with_html_d import app, db, Product

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Creating tables
        yield client


def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 25})
    assert response.status_code == 302  # Check for redirect
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.stock == 25


def test_record_sale(client):
    product = Product(name='Product2', stock=20)
    db.session.add(product)
    db.session.commit()
    response = client.post('/record_sale', data={'product_id': product.id, 'quantity': 5})
    assert response.status_code == 302  # Check for redirect
    updated_product = Product.query.get(product.id)
    assert updated_product.sales == 5