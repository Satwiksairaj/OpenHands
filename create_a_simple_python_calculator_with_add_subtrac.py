"""
create_a_simple_python_calculator_with_add_subtrac.py
=============
Simple Calculator Application

Usage:
    python create_a_simple_python_calculator_with_add_subtrac.py

Author: Autonomous Agent
"""
from typing import Any, Dict, List, Optional, Tuple

# Third-party imports
from flask import Flask, request, jsonify, render_template

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def index() -> Tuple[Any, int]:
    """Home page endpoint."""
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

@app.route('/add', methods=['POST'])
def add() -> Tuple[Any, int]:
    data = request.json
    result = data['a'] + data['b']
    return jsonify({'result': result}), 200

@app.route('/subtract', methods=['POST'])
def subtract() -> Tuple[Any, int]:
    data = request.json
    result = data['a'] - data['b']
    return jsonify({'result': result}), 200

@app.route('/multiply', methods=['POST'])
def multiply() -> Tuple[Any, int]:
    data = request.json
    result = data['a'] * data['b']
    return jsonify({'result': result}), 200

@app.route('/divide', methods=['POST'])
def divide() -> Tuple[Any, int]:
    data = request.json
    if data['b'] == 0:
        return jsonify({'error': 'Division by zero'}), 400
    if data['b'] == 0:
        return jsonify({'error': 'Division by zero'}), 400
    result = data['a'] / data['b']
    return jsonify({'result': result}), 200


@app.route('/calculate', methods=['POST'])
def calculate() -> Tuple[Any, int]:
    """Perform a calculation based on operation provided."""
    data = request.json
    operation = data.get('operation')
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        return jsonify({'error': 'Invalid operation'}), 400
    a = data['a']
    b = data['b']
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = a / b
    return jsonify({'result': result}), 200

# =============================================================================
# ERROR HANDLERS - Must be SEPARATE from routes!
# =============================================================================

@app.errorhandler(404)
def not_found(error) -> Tuple[Any, int]:
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error) -> Tuple[Any, int]:
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)