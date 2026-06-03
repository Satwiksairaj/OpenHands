import json
from flask import Flask, render_template, request

app = Flask(__name__)

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
class Order:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
class AdminDashboard:
    def __init__(self):
        self.products = []  # type: List[Product]
        self.orders = []  # type: List[Order]

    def add_product(self, product: Product):
        self.products.append(product)
    def create_order(self, product_name: str, quantity: int):
        for product in self.products:
            if product.name == product_name and product.stock >= quantity:
                product.stock -= quantity
                order = Order(product, quantity)
                self.orders.append(order)
                return order
        raise ValueError("Insufficient stock or product not found.")
    def get_stock_levels(self):
        return {product.name: product.stock for product in self.products}
    def get_sales_report(self):
        return [vars(order) for order in self.orders]

admin_dashboard = AdminDashboard()

# Sample Data
admin_dashboard.add_product(Product("Laptop", 999.99, 10))
admin_dashboard.add_product(Product("Smartphone", 499.99, 15))

@app.route('/')
def index():
    stock_levels = admin_dashboard.get_stock_levels()
    return render_template('index.html', stock_levels=stock_levels)

@app.route('/order', methods=['POST'])
def order():
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    try:
        order = admin_dashboard.create_order(product_name, quantity)
        return json.dumps({'success': True, 'order': vars(order)})
    except ValueError as e:
        return json.dumps({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
