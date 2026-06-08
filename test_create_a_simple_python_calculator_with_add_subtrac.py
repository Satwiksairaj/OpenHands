import json
import unittest
from create_a_simple_python_calculator_with_add_subtrac import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        """Create a test client for the app."""
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.post('/add', json={'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 3)

    def test_subtract(self):
        response = self.app.post('/subtract', json={'a': 5, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 3)

    def test_multiply(self):
        response = self.app.post('/multiply', json={'a': 3, 'b': 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 12)

    def test_divide(self):
        response = self.app.post('/divide', json={'a': 10, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 5)

    def test_calculate(self):
        response = self.app.post('/calculate', json={'operation': 'add', 'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 3)

    def test_invalid_operation(self):
        response = self.app.post('/calculate', json={'operation': 'invalid', 'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid operation', json.loads(response.data)['error'])

    def test_divide_by_zero(self):
        response = self.app.post('/divide', json={'a': 10, 'b': 0})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Division by zero', json.loads(response.data)['error'])

if __name__ == '__main__':
    unittest.main()