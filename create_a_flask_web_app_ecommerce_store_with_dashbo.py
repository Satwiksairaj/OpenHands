from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce_store.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    product_name = request.form.get('name')
    product_stock = request.form.get('stock')
    product_price = request.form.get('price')
    new_product = Product(name=product_name, stock=product_stock, price=product_price)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_id = request.form.get('product_id')
    quantity_sold = request.form.get('quantity')
    sale = Sale(product_id=product_id, quantity=quantity_sold)
    db.session.add(sale)
    db.session.commit()
    return redirect(url_for('index'))

# Initialize database
with app.app_context():
    db.create_all()  # Create database tables

# Run the Flask application

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_web_app_ecommerce_store_with_dashbo.py
# Then open: http://127.0.0.1:5000
# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_web_app_ecommerce_store_with_dashbo.py
# Then open: http://127.0.0.1:5000