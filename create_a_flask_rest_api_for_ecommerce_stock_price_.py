"""
create_a_flask_rest_api_for_ecommerce_stock_price_.py
=============
A Flask REST API for e-commerce stock price tracking.

Usage:
    python create_a_flask_rest_api_for_ecommerce_stock_price_.py

Author: Autonomous Agent
"""
from typing import Any, Dict, List, Optional, Tuple

# Third-party imports
from flask import Flask, request, jsonify, render_template

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# =============================================================================
# MODELS
# =============================================================================

class Product:
    """Product model for e-commerce."
    def __init__(self, id: int, name: str, price: float) -> None:
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'name': self.name, 'price': self.price}

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def index() -> Tuple[Any, int]:
    """Home page endpoint."
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

@app.route('/products', methods=['POST'])
def create_product() -> Tuple[Any, int]:
    """Create a new product."
    data = request.get_json()  # Validate input data as needed
    product = Product(id=data['id'], name=data['name'], price=data['price'])
    return jsonify(product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> Tuple[Any, int]:
    """Get a product by ID."
    # Here we would normally fetch from a database. This is a placeholder.
    return jsonify({'id': product_id, 'name': 'Sample Product', 'price': 29.99}), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Tuple[Any, int]:
    """Update a product by ID."
    data = request.get_json()  # Validate input & update in database
    return jsonify({'status': 'success', 'id': product_id}), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Tuple[Any, int]:
    """Delete a product by ID."
    return jsonify({'status': 'success', 'id': product_id}), 204


# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(404)
def not_found(error) -> Tuple[Any, int]:
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error) -> Tuple[Any, int]:
    return jsonify({'error': 'Internal server error'}), 500

# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)