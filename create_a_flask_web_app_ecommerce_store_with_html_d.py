from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products and sales
products = {"Sample Product": 10, "Another Product": 5}
app.secret_key = 'your_secret_key'
sales = []

@app.route('/sell_product', methods=['GET'])
def sell_product():
        product_name = request.args.get('product_name')
        if product_name and products.get(product_name):
            available_stock = products[product_name]
            return render_template('sell_product.html', product_name=product_name, available_stock=available_stock)
        return 'Product not available.'

@app.route('/')
def index():
    return render_template('dashboard.html', products=products, sales=sales)

@app.route('/add_product', methods=['POST'])
def add_product():
    product_name = request.form.get('product_name')
    stock_level = request.form.get('stock_level', type=int)
    if product_name and stock_level is not None:
        products[product_name] = stock_level
    return redirect(url_for('index'))

@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity', type=int)
    if product_name in products and quantity:
        sales.append({'product': product_name, 'quantity': quantity})
        products[product_name] -= quantity
    return redirect(url_for('index'))

# HOW TO RUN:


if __name__ == '__main__':
    app.run(debug=True)