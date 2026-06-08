from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from models import Product, Sale
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    stock = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=0)])

class SaleForm(FlaskForm):
    product = StringField('Product', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    customer = StringField('Customer Name', validators=[DataRequired()])

@app.route('/')
def dashboard():
    products = Product.query.all()
    total_inventory_value = sum(p.price * p.stock_quantity for p in products)
    return render_template('index.html', products=products, total_inventory_value=total_inventory_value)

@app.route('/sales', methods=['GET', 'POST'])
def sales():
    form = SaleForm()
    if form.validate_on_submit():
        product = Product.query.filter_by(name=form.product.data).first()
        if product and product.stock_quantity >= form.quantity.data:
            sale = Sale(product_id=product.id,
                        quantity=form.quantity.data,
                        customer_name=form.customer.data,
                        revenue=form.quantity.data * product.price)
            product.stock_quantity -= form.quantity.data
            db.session.add(sale)
            db.session.commit()
            flash('Sale recorded successfully!', 'success')
            return redirect(url_for('sales'))
        else:
            flash('Insufficient stock or product not found', 'danger')
    return render_template('sales.html', form=form)

@app.route('/products', methods=['GET', 'POST'])
def products():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product.query.filter_by(name=form.name.data).first()
        if not product:
            product = Product(name=form.name.data,
                              category=form.category.data,
                              price=form.price.data,
                              stock_quantity=form.stock.data)
            db.session.add(product)
        else:
            product.price = form.price.data
            product.stock_quantity = form.stock.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('products'))
    return render_template('products.html', form=form)

@app.route('/api/stats')
def api_stats():
    products = Product.query.all()
    total_products = len(products)
    total_stock_value = sum(p.price * p.stock_quantity for p in products)
    total_revenue = sum(s.revenue for s in Sale.query.all())
    top_selling_products = db.session.query(Product.name, db.func.sum(Sale.quantity))\
        .join(Sale, Product.id == Sale.product_id)\
        .group_by(Product.name)\
        .order_by(db.func.sum(Sale.quantity).desc())\
        .limit(5).all()
    low_stock_alerts = [p for p in products if p.stock_quantity < 10]
    return jsonify({
        'totalProducts': total_products,
        'totalStockValue': total_stock_value,
        'totalRevenue': total_revenue,
        'topSellingProducts': [dict(name=prod[0], quantity=prod[1]) for prod in top_selling_products],
        'lowStockAlerts': [p.name for p in low_stock_alerts]
    })


def seed_data():
    if Product.query.count() == 0:  # Avoid seeding if already done
        sample_products = [
            Product(name='Laptop', category='Electronics', price=999.99, stock_quantity=50),
            Product(name='Smartphone', category='Electronics', price=499.99, stock_quantity=100),
            Product(name='Headphones', category='Electronics', price=99.99, stock_quantity=150),
            Product(name='Refrigerator', category='Appliances', price=1249.99, stock_quantity=20),
            Product(name='Microwave', category='Appliances', price=199.99, stock_quantity=75),
            Product(name='Oven', category='Appliances', price=649.99, stock_quantity=40),
            Product(name='Running Shoes', category='Apparel', price=89.99, stock_quantity=200),
            Product(name='Jacket', category='Apparel', price=149.99, stock_quantity=120),
            Product(name='T-Shirt', category='Apparel', price=29.99, stock_quantity=300),
            Product(name='Jeans', category='Apparel', price=59.99, stock_quantity=100)
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()
        print('Seed data inserted into the database.')

if __name__ == '__main__':
    db.create_all()
    seed_data()
    app.run(debug=True)