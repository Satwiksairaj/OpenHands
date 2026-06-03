from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route for the index page
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)  # Render the index template with product data.

# Route to add a product
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name') if request.form.get('name') else "Unnamed Product"
    stock = request.form.get('stock')
    if stock is not None:
        stock = int(stock)
    new_product = Product(name=name, stock=stock if stock is not None else 0)
    print(f'Adding Product: {name}, Stock: {stock}')
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

# Route to record a sale
@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_id = request.form.get('product_id')
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', type=int)
    product.sales += quantity
    db.session.commit()
    return redirect(url_for('index'))

# Start the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_web_app_ecommerce_store_with_html_d.py
# Then open: http://127.0.0.1:5000

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route for the index page
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)  # Render the index template with product data.

# Route to add a product
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name') if request.form.get('name') else "Unnamed Product"
    stock = request.form.get('stock')
    if stock is not None:
        stock = int(stock)
    new_product = Product(name=name, stock=stock if stock is not None else 0)
    print(f'Adding Product: {name}, Stock: {stock}')
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

# Route to record a sale
@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_id = request.form.get('product_id')
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', type=int)
    product.sales += quantity
    db.session.commit()
    return redirect(url_for('index'))

# Start the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_web_app_ecommerce_store_with_html_d.py
# Then open: http://127.0.0.1:5000
