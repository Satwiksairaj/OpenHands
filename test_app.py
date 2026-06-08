import pytest
from app import app, db
from models import Product, Sale

@pytest.fixture(scope='module')
def test_client():
    # Set up
    app.config['TESTING'] = True
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    yield testing_client  # this is where the testing happens!

    # Tear down
    ctx.pop()

# Basic test case example
def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Ecommerce Dashboard' in response.data