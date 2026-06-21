"""
Flask E-Commerce Store with Dashboard
======================================
A simple web app showing stock levels and sales data,
with routes for adding products and recording sales.

HOW TO RUN:
    pip install -r requirements.txt
    python create_a_flask_web_app_ecommerce_store_with_dashbo.py
    Then open: http://127.0.0.1:5000
"""
from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict

app = Flask(__name__)

# In-memory storage for products (name -> stock level) and sales history
products = defaultdict(int)
sales = []


@app.route('/')
def home():
    """Home page - redirects to dashboard."""
    return render_template('dashboard.html', products=products, sales=sales)


@app.route('/dashboard')
def dashboard():
    """Dashboard showing stock levels and sales data."""
    return render_template('dashboard.html', products=products, sales=sales)


@app.route('/add_product', methods=['POST'])
def add_product():
    """Add a new product or update stock level."""
    product_name = request.form.get('product_name', '').strip()
    stock_level = request.form.get('stock_level', 0)
    
    try:
        stock_level = int(stock_level)
    except ValueError:
        stock_level = 0
    
    if product_name and stock_level >= 0:
        products[product_name] = stock_level
    
    return redirect(url_for('home'))


@app.route('/record_sale', methods=['POST'])
def record_sale():
    """Record a sale for a product (decrements stock)."""
    product_name = request.form.get('product_name', '').strip()
    
    if product_name in products and products[product_name] > 0:
        sales.append(product_name)
        products[product_name] -= 1
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)