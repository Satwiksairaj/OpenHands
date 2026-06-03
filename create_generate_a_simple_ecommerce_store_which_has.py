import json
from flask import Flask, render_template, request, redirect
from jinja2 import TemplateNotFound

app = Flask(__name__)

# Sample data to simulate stock and sales data
ecommerce_data = {
    'stock': [
        {'id': 1, 'name': 'Product A', 'price': 29.99, 'quantity': 100},
        {'id': 2, 'name': 'Product B', 'price': 49.99, 'quantity': 200},
        {'id': 3, 'name': 'Product C', 'price': 19.99, 'quantity': 150}
    ],
    'sales': [
        {'id': 1, 'product_id': 1, 'quantity_sold': 3},
        {'id': 2, 'product_id': 2, 'quantity_sold': 1},
        {'id': 3, 'product_id': 3, 'quantity_sold': 2}
    ]
}

@app.route('/')
def dashboard():
    total_sales = sum(sale['quantity_sold'] for sale in ecommerce_data['sales'])
    try:
        return render_template('dashboard.html', stock=ecommerce_data['stock'], sales=ecommerce_data['sales'], total_sales=total_sales)
    except TemplateNotFound:
        return "Template not found, please ensure dashboard.html exists."

if __name__ == '__main__':
    app.run(debug=True)
