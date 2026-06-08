from flask import Flask, render_template, request, jsonify
from models import db, Product, Sale
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    # Seed data
    if not Product.query.first():
        sample_products = [
            Product(name="Product 1", price=10.99, stock_quantity=100, category="Category A"),
            Product(name="Product 2", price=15.99, stock_quantity=80, category="Category A"),
            Product(name="Product 3", price=9.99, stock_quantity=150, category="Category B"),
            Product(name="Product 4", price=12.50, stock_quantity=50, category="Category B"),
            Product(name="Product 5", price=5.00, stock_quantity=20, category="Category C"),
            Product(name="Product 6", price=7.75, stock_quantity=70, category="Category C"),
            Product(name="Product 7", price=2.99, stock_quantity=200, category="Category B"),
            Product(name="Product 8", price=22.00, stock_quantity=90, category="Category A"),
            Product(name="Product 9", price=18.50, stock_quantity=60, category="Category C"),
            Product(name="Product 10", price=6.50, stock_quantity=15, category="Category A"),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
@app.route('/sales', methods=['POST'])
def record_sale():
    data = request.form
    product_id = data.get('product_id')
    quantity = int(data.get('quantity', 0))
    product = db.session.get(Product, product_id)
    if product and quantity <= product.stock_quantity:
        product.stock_quantity -= quantity
        revenue = product.price * quantity
        sale = Sale(product_id=product.id, quantity=quantity, revenue=revenue, timestamp=datetime.now())
        db.session.add(sale)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Sale recorded'}), 200
    return jsonify({'success': False, 'message': 'Sale recording failed'}), 400
@app.route('/products', methods=['GET', 'POST'])
@app.route('/api/stats')
def api_stats():
    total_products = Product.query.count()
    total_stock_value = db.session.query(db.func.sum(Product.price * Product.stock_quantity)).scalar() or 0
    total_revenue = db.session.query(db.func.sum(Sale.revenue)).scalar() or 0

    top_selling = db.session.query(Product.name, db.func.sum(Sale.quantity).label('total_sold'))
    top_selling = top_selling.join(Sale, Sale.product_id == Product.id)
    top_selling = top_selling.group_by(Product.id)
    top_selling = top_selling.order_by(db.desc('total_sold'))
    top_selling = top_selling.limit(5)
    top_selling = top_selling.all()

    low_stock_alerts = Product.query.filter(Product.stock_quantity < 10).all()

    return jsonify({
        'total_products': total_products,
        'total_stock_value': total_stock_value,
        'total_revenue': total_revenue,
        'top_selling': [{'name': prod.name, 'total_sold': total_sold} for prod, total_sold in top_selling],
        'low_stock_alerts': [{'name': prod.name, 'stock_quantity': prod.stock_quantity} for prod in low_stock_alerts],
    })

def run_app():
    app.run(debug=True)

if __name__ == '__main__':
    run_app()