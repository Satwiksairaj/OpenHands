from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    return render_template('index.html', products=products)

# Route to add a product
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name', 'Unnamed Product')
    stock = int(request.form.get('stock', 0))
    new_product = Product(name=name, stock=stock)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

# Route to record a sale
@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 0))
    product = Product.query.get_or_404(product_id)
    if product.stock >= quantity:
        product.stock -= quantity
        product.sales += quantity
        db.session.commit()
    return redirect(url_for('index'))

# Start the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
