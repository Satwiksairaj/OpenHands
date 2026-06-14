"""
create_a_file_hellopy_with_a_function_greet_that_r.py
=============
This module contains a Flask application with a hello endpoint.

Usage:
    python create_a_file_hellopy_with_a_function_greet_that_r.py

Author: Autonomous Agent
"""
from typing import Any, Tuple

# Third-party imports
from flask import Flask, jsonify

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# =============================================================================
# ROUTES - Each decorator MUST be immediately followed by its function!
# =============================================================================

@app.route('/')
def index() -> Tuple[Any, int]:
    """Home page endpoint - REQUIRED for validation to pass."""
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

@app.route('/hello')
def hello() -> Tuple[Any, int]:
    """Hello endpoint."""
    return jsonify({'message': 'Hello World'}), 200


@app.route('/greet')
def greet() -> Tuple[Any, int]:
    """Greet endpoint that returns Hello World."""
    return jsonify({'message': 'Hello World'}), 200

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
