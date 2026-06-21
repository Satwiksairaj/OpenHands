import pytest
import base64
from add_rolebased_access_control import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_admin_access(client):
    response = client.get('/admin', auth=('admin', 'admin_password'))
pass


def test_user_access(client):
def test_user_access(client):
    # Testing user role access to admin route
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data

    # Testing admin access with wrong credentials
    response = client.get('/admin', auth=('admin', 'wrong_password'))
    assert response.status_code == 401
    assert b'Authentication required!' in response.data
def test_user_access(client):
    # Testing user role access to admin route
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data

    # Testing admin access with wrong credentials
    response = client.get('/admin', auth=('admin', 'wrong_password'))
    assert response.status_code == 401
    assert b'Authentication required!' in response.data
def test_user_access(client):
    # Testing user role access to admin route
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data

    # Testing admin access with wrong credentials
    response = client.get('/admin', auth=('admin', 'wrong_password'))
    assert response.status_code == 401
    assert b'Authentication required!' in response.data
def test_user_access(client):
    # Testing user role access to admin route
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data

    # Testing admin access with wrong credentials
    response = client.get('/admin', auth=('admin', 'wrong_password'))
    assert response.status_code == 401
    assert b'Authentication required!' in response.data
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data

    # Removed duplicate auth checks
    assert response.status_code == 401
    assert b'Authentication required!' in response.data
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data
    response = client.get('/admin', auth=('user', 'user_password'))
    assert response.status_code == 403
    assert b'Access denied for this role!' in response.data


def test_unauthorized_access(client):
    response = client.get('/admin')
    assert response.status_code == 401
    assert b'Authentication required!' in response.data