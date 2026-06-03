import json
from typing import List, Dict

class EcommerceStore:
    def __init__(self):
        self.stock: Dict[str, int] = {}  # Product name and its quantity
        self.sales_data: List[Dict[str, float]] = []  # Sales records

    def add_product(self, product_name: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.stock[product_name] = self.stock.get(product_name, 0) + quantity
    def sell_product(self, product_name: str, quantity: int) -> None:
        if product_name not in self.stock:
            raise ValueError(f'Product {product_name} not found')
        if self.stock[product_name] < quantity:
            raise ValueError('Not enough stock available')
        self.stock[product_name] -= quantity
        self.sales_data.append({'product_name': product_name, 'quantity': quantity})
    def get_stock(self) -> Dict[str, int]:
        return self.stock
    def get_sales_data(self) -> List[Dict[str, float]]:
        return self.sales_data
    def dashboard(self) -> str:
        return json.dumps({'stock': self.get_stock(), 'sales_data': self.get_sales_data()}, indent=4)
