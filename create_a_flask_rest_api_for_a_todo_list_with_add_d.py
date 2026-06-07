"""
Todo List REST API

A clean Flask REST API with add, delete, and list endpoints.
Demonstrates production-quality code structure.

Author: Autonomous Agent
"""
from typing import Any, Dict, List, Tuple

from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

# ── App Configuration ─────────────────────────────────────────────────────────
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ── Models ────────────────────────────────────────────────────────────────────
class Todo(db.Model):
    """Todo item model."""
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f'Todo(id={self.id}, task={self.task})'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {'id': self.id, 'task': self.task}


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/')
def home() -> Tuple[Response, int]:
    """Home endpoint with API information."""
    return jsonify({
        'message': 'Welcome to the Todo API!',
        'endpoints': {
            'GET /': 'This help message',
            'GET /todos': 'List all todos',
            'POST /todos': 'Add a new todo (JSON body: {"task": "..."})',
            'DELETE /todos/<id>': 'Delete a todo by ID'
        }
    }), 200


@app.route('/todos', methods=['GET'])
def list_todos() -> Tuple[Response, int]:
    """List all todo items."""
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200


@app.route('/todos', methods=['POST'])
def add_todo() -> Tuple[Response, int]:
    """Add a new todo item.
    
    Expects JSON body: {"task": "your task description"}
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body must be JSON'}), 400
        
        task = data.get('task')
        if not task or not task.strip():
            return jsonify({'error': 'Task is required and cannot be empty'}), 400
        
        new_todo = Todo(task=task.strip())
        db.session.add(new_todo)
        db.session.commit()
        
        return jsonify({
            'message': 'Todo added successfully',
            'todo': new_todo.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int) -> Tuple[Response, int]:
    """Delete a todo item by ID."""
    try:
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return jsonify({'error': f'Todo with id {todo_id} not found'}), 404
        
        db.session.delete(todo)
        db.session.commit()
        
        return jsonify({'message': f'Todo {todo_id} deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)


# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_rest_api_for_a_todo_list_with_add_d.py
# Then open: http://127.0.0.1:5000