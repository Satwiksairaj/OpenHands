"""
create_a_simple_python_calculator_with_add_and_sub.py
=============
A simple Python calculator with add and subtract functions.

Usage:
    python create_a_simple_python_calculator_with_add_and_sub.py

Author: Autonomous Agent
"""
from typing import Any, Dict, Tuple

# Third-party imports
from flask import Flask, request, jsonify

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
    """Add two numbers."""
    data = request.json
    try:
        result = data['a'] + data['b']
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Keys a and b are required.'}), 400

@app.route('/subtract', methods=['POST'])
def subtract() -> Tuple[Any, int]:
    """Subtract two numbers."""
    data = request.json
    try:
        result = data['a'] - data['b']
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Keys a and b are required.'}), 400

# =============================================================================
# ERROR HANDLERS
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