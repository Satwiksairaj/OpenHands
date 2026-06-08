"""
create_a_simple_add_function_in_mathutilspy_that_a.py
=====================
Main application that includes a simple add function in math_utils.

Usage:
    python create_a_simple_add_function_in_mathutilspy_that_a.py

Author: Autonomous Agent
"""
from typing import Any, Tuple

# Third-party imports
from flask import Flask, request, jsonify

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# =============================================================================
# ROUTES - Each decorator MUST be immediately followed by its function!
# =============================================================================

@app.route('/')
def index() -> Tuple[Any, int]:
    """Home page endpoint."""
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200
    


@app.route('/add', methods=['POST'])
def add() -> Tuple[Any, int]:
    """Add two numbers provided in JSON payload."""
    data = request.get_json()
    x = data.get('num1')
    y = data.get('num2')
    if x is None or y is None:
        return jsonify({'error': 'Invalid input, please provide num1 and num2.'}), 400
    result = x + y
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
# ENTRY POINT - Must be at the VERY END of the file!
# =============================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)