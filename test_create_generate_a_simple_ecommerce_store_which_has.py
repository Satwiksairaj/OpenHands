import pytest
from create_generate_a_simple_ecommerce_store_which_has import EcommerceStore

class TestEcommerceStore:
    def setup_method(self):
        self.store = EcommerceStore()

    def test_add_product(self):
        self.store.add_product('Widget', 10)
        assert self.store.get_stock()['Widget'] == 10
    def test_sell_product(self):
        self.store.add_product('Widget', 10)
        self.store.sell_product('Widget', 5)
        assert self.store.get_stock()['Widget'] == 5
    def test_sell_product_not_found(self):
        with pytest.raises(ValueError):
            self.store.sell_product('NonExistentProduct', 1)
    def test_sell_product_insufficient_stock(self):
        self.store.add_product('Widget', 5)
        with pytest.raises(ValueError):
            self.store.sell_product('Widget', 10)
    def test_negative_quantity(self):
        with pytest.raises(ValueError):
            self.store.add_product('Widget', -5)
    def test_dashboard(self):
        self.store.add_product('Widget', 10)
        self.store.sell_product('Widget', 2)
        expected_dashboard = {'stock': {'Widget': 8}, 'sales_data': [{'product_name': 'Widget', 'quantity': 2}]}
        assert self.store.dashboard() == expected_dashboard
