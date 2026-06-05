import pytest
from create_a_flask_web_app_ecommerce_store_with_dashbo import app, db, Product, Sale

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_product(client):
    response = client.post('/add_product', data={'name': 'Test Product', 'stock': 10, 'price': 19.99})
    assert response.status_code == 302  # Check if redirected
    product = Product.query.first()
    assert product.name == 'Test Product'
    assert product.stock == 10
    assert product.price == 19.99


def test_record_sale(client):
    # First, add a product
    client.post('/add_product', data={'name': 'Test Product', 'stock': 10, 'price': 19.99})
    product = Product.query.first()
    # Now, record a sale
    response = client.post('/record_sale', data={'product_id': product.id, 'quantity': 1})
    assert response.status_code == 302  # Check if redirected
    sale = Sale.query.first()
    assert sale.product_id == product.id
    assert sale.quantity == 1