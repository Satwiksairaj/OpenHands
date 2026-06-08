import pytest
from app import app, db, Product, Sale

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_sales_endpoint(client):
    # Test logic for sales endpoint
    response = client.post('/sales', data={'product_id': 1, 'quantity': 2})
    assert response.status_code == 200


def test_api_stats_endpoint(client):
    response = client.get('/api/stats')
    assert response.status_code == 200
    assert 'total_products' in response.json