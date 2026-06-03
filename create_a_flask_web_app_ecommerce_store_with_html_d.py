from flask import Flask, render_template, request, redirect, url_for
from flask.wrappers import Response
from typing import List, Dict

app = Flask(__name__)

# In-memory data storage for simplicity
products: List[Dict] = []
product_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    global product_id_counter
    if request.method == 'POST':
        product_name = request.form['name']
        stock_level = request.form['stock']

        # Add new product to the list
        products.append({
            'id': product_id_counter,
            'name': product_name,
            'stock': int(stock_level),
        })
        product_id_counter += 1
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/record_sale', methods=['POST'])
def record_sale():
    product_id = int(request.form['product_id'])
    quantity_sold = int(request.form['quantity'])

    for product in products:
        if product['id'] == product_id:
            product['stock'] -= quantity_sold
            break

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
