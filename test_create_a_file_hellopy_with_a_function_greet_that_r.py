import unittest
from create_a_file_hellopy_with_a_function_greet_that_r import app

class HelloWorldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok', 'message': 'API is running'})

    def test_greet(self):
        response = self.app.get('/greet')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello World'})

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello World'})

if __name__ == '__main__':
    unittest.main()