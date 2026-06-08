from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import func
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from models import Product, Sale

# Home route or Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Dashboard route
def calculate_inventory_value(products):
    return sum(product.price * product.stock for product in products)

@app.route('/dashboard')
def dashboard():
    products = Product.query.all()
    total_inventory_value = calculate_inventory_value(products)
    sales = Sale.query.all()
    return render_template('dashboard.html', products=products, total_inventory_value=total_inventory_value, sales=sales)

# Sales route
@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        customer_name = request.form.get('customer_name')
        product = Product.query.get(product_id)

        if product and quantity <= product.stock:
            new_sale = Sale(product_id=product_id, quantity=quantity,
                            customer_name=customer_name, date=datetime.utcnow(),
                            revenue=product.price * quantity)
            product.stock -= quantity
            db.session.add(new_sale)
            db.session.commit()
            flash('Sale recorded successfully!', 'success')
        else:
            flash('Insufficient stock for this product.', 'danger')

        return redirect(url_for('sales'))
    if request.method == 'GET' or not request.form:
        products = Product.query.all()
        return render_template('sales.html', products=products)

    # API for statistics and alerts
@app.route('/api/stats')
def api_stats():
    total_products = Product.query.count()
    stock_value = db.session.query(func.sum(Product.price * Product.stock)).scalar() or 0
    total_revenue = db.session.query(func.sum(Sale.revenue)).scalar() or 0
    top_selling_products = db.session.query(Product.name, func.sum(Sale.quantity).label('total_sold'))\
        .join(Sale)\
        .group_by(Product.id)\
        .order_by(func.sum(Sale.quantity).desc())\
        .limit(5).all()
    low_stock_alerts = Product.query.filter(Product.stock < 5).all()

    return jsonify({
        'total_products': total_products,
        'stock_value': stock_value,
        'total_revenue': total_revenue,
        'top_selling_products': [{'name': product.name, 'total_sold': total_sold} for product, total_sold in top_selling_products],
        'low_stock_alerts': [{'name': product.name, 'stock': product.stock} for product in low_stock_alerts]
    })

    products = Product.query.all()
    return render_template('sales.html', products=products)

# Products route
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        name = request.form.get('name')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))
        category = request.form.get('category')

        if product_id:  # Update existing product
            product = Product.query.get(product_id)
            if product:
                product.name = name
                product.price = price
                product.stock = stock
                product.category = category
                flash('Product updated successfully!', 'success')
        else:  # Add new product
            new_product = Product(name=name, price=price, stock=stock, category=category)
            db.session.add(new_product)
            flash('New product added successfully!', 'success')

        db.session.commit()
        return redirect(url_for('products'))

    products = Product.query.all()
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
