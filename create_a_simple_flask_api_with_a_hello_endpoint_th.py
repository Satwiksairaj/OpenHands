"""Simple Flask API with a /hello endpoint that returns a greeting."""
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
@app.route('/')
def home() -> str:
    """Return a welcome message."""
    return 'Welcome to the Flask API!'

@app.route('/hello')
def hello() -> str:
    """Return a greeting message."""
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)
# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_simple_flask_api_with_a_hello_endpoint_th.py
# Then open: http://127.0.0.1:5000