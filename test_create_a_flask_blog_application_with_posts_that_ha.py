import unittest
from create_a_flask_blog_application_with_posts_that_ha import app

class BlogAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Blog Posts', result.data)
    def test_create_post(self):
        result = self.app.post('/post/new', data={'title': 'Test Post', 'content': 'Test content.'})
        self.assertEqual(result.status_code, 201)
        self.assertIn(b'Test Post', result.data)
    def test_view_post(self):
        self.app.post('/post/new', data={'title': 'Test Post', 'content': 'Test content.'})
        result = self.app.get('/post/0')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Test Post', result.data)

if __name__ == '__main__':
    unittest.main()