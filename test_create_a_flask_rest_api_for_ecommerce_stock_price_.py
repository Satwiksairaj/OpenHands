import unittest
from create_a_flask_rest_api_for_ecommerce_stock_price_ import app

class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'API is running', response.data)

    def test_create_product(self):
        response = self.app.post('/products', json={'id': 1, 'name': 'Test Product', 'price': 99.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Test Product', response.data)

    def test_get_product(self):
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sample Product', response.data)

    def test_update_product(self):
        response = self.app.put('/products/1', json={'name': 'Updated Product', 'price': 19.99})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_delete_product(self):
        response = self.app.delete('/products/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()