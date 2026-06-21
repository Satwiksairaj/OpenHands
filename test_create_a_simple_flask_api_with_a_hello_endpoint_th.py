import pytest
from create_a_simple_flask_api_with_a_hello_endpoint_th import app

def test_hello():
    """Test the /hello endpoint."""
    client = app.test_client()
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200