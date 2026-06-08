from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    product = db.relationship('Product', backref=db.backref('sales', lazy=True))

    def __repr__(self):
        return f'<Sale {self.product_id}>'