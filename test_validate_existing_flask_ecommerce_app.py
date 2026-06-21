import pytest
from validate_existing_flask_ecommerce_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_validate_app_valid(client):
    response = client.post('/validate', json={'app_path': 'C:/Users/Satwik.Anand/Desktop/autonomous-agent/workspace/OpenHands/instance/ecommerce.db'})
    assert response.status_code == 200
    assert response.json['success'] == 'App path is valid!'
def test_validate_app_invalid(client):
    response = client.post('/validate', json={'app_path': 'C:/nonexistent/path'})
    assert response.status_code == 400
    assert response.json['error'] == 'App path does not exist!'
