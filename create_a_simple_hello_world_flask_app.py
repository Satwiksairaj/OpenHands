from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', product=None)

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_simple_hello_world_flask_app.py
# Then open: http://127.0.0.1:5000
