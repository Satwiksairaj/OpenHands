import pytest  
from create_a_flask_rest_api_for_a_todo_list_with_add_d import app, db, Todo  

@pytest.fixture(scope='module')  
def test_client():  
    testing_client = app.test_client()  
    app.config['TESTING'] = True  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
    db.create_all()  
    yield testing_client  
    db.drop_all()  

def test_add_todo(test_client):  
    response = test_client.post('/todos', json={'task': 'Test task'})  
    assert response.status_code == 201  
    assert response.json['message'] == 'Todo added'  
def test_list_todos(test_client):  
    response = test_client.get('/todos')  
    assert response.status_code == 200  
    assert isinstance(response.json, list)  
def test_delete_todo(test_client):  
    response = test_client.post('/todos', json={'task': 'Task to delete'})  
    todo_id = response.json['id']  
    delete_response = test_client.delete(f'/todos/{todo_id}')  
    assert delete_response.status_code == 200  
    assert delete_response.json['message'] == 'Todo deleted'  
    
    not_found_response = test_client.delete(f'/todos/{todo_id}')  
    assert not_found_response.status_code == 404  
    assert not_found_response.json['error'] == 'Todo not found'  
