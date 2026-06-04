from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Updated implementation with additional features
    total_price = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return 'Welcome to the E-commerce Store!'
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

@app.route('/')
def dashboard():
    products = Product.query.all()
    sales = Sale.query.all()
    total_sales = sum(sale.total_price for sale in sales)
    return render_template('dashboard.html', products=products, total_sales=total_sales)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        stock = request.form['stock']
        price = float(request.form['price'])
        new_product = Product(name=name, stock=stock, price=price)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('dashboard'))
    return render_template('add_product.html')

@app.route('/record_sale', methods=['GET', 'POST'])
def record_sale():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        product = Product.query.get(product_id)
        if product:
            total_price = float(product.price) * quantity
            new_sale = Sale(product_id=product_id, quantity=quantity, total_price=total_price)
            db.session.add(new_sale)
            product.stock -= quantity
            db.session.commit()
            flash('Sale recorded successfully!')
        else:
            flash('Product not found!')
        return redirect(url_for('dashboard'))
    products = Product.query.all()
    return render_template('record_sale.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_web_app_ecommerce_store_with_html_d.py
# Then open: http://127.0.0.1:5000