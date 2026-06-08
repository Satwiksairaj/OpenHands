from app import db
from models import Product

def seed_data():
    sample_products = [
        {'name': 'Laptop', 'price': 999.99, 'stock': 15, 'category': 'Electronics'},
        {'name': 'Smartphone', 'price': 599.99, 'stock': 30, 'category': 'Electronics'},
        {'name': 'Headphones', 'price': 199.99, 'stock': 20, 'category': 'Accessories'},
        {'name': 'Coffee Maker', 'price': 49.99, 'stock': 25, 'category': 'Home Appliances'},
        {'name': 'Blender', 'price': 39.99, 'stock': 10, 'category': 'Home Appliances'},
        {'name': 'E-book Reader', 'price': 129.99, 'stock': 18, 'category': 'Electronics'},
        {'name': 'Office Chair', 'price': 89.99, 'stock': 12, 'category': 'Furniture'},
        {'name': 'Bookcase', 'price': 79.99, 'stock': 8, 'category': 'Furniture'},
        {'name': 'Desk', 'price': 149.99, 'stock': 5, 'category': 'Furniture'},
        {'name': 'Bluetooth Speaker', 'price': 49.99, 'stock': 22, 'category': 'Accessories'},
    ]

    for product in sample_products:
        new_product = Product(name=product['name'], price=product['price'],
                              stock=product['stock'], category=product['category'])
        db.session.add(new_product)
    db.session.commit()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        seed_data()
        print("Database seeded with sample product data.")
