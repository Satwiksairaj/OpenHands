"""
test_create_a_simple_add_function_in_mathutilspy_that_a.py
=====================
Unit tests for the add function in math_utils.

Usage:
    Execute this file to run the tests.
"""
import json
from typing import Any
from flask import Flask
from flask import jsonify
import unittest

# Assuming the app is imported from the main file
from create_a_simple_add_function_in_mathutilspy_that_a import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_add(self) -> None:
        response = self.client.post('/add', json={'num1': 2, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 5})

    def test_add_invalid_input(self) -> None:
        response = self.client.post('/add', json={'a': 'two', 'b': 3})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid input, please provide num1 and num2.'})

if __name__ == '__main__':
    unittest.main()