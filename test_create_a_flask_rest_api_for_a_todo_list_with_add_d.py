import pytest
import json
from create_a_flask_rest_api_for_a_todo_list_with_add_d import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_todo(client):
    response = client.post('/todos', json={'task': 'Test task'})
    assert response.status_code == 201
    assert response.json['message'] == 'Todo added'
def test_list_todos(client):
    client.post('/todos', json={'task': 'Another test task'})
    response = client.get('/todos')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
def test_delete_todo(client):
    response = client.post('/todos', json={'task': 'Task to delete'})
    todo_id = json.loads(response.data)['id']
    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Todo deleted'
def test_delete_nonexistent_todo(client):
    response = client.delete('/todos/99999')  # Assuming this ID does not exist
    assert response.status_code == 404
    assert b'Todo not found' in response.data