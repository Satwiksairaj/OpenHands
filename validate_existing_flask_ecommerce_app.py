from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_app():
    app_path = request.json.get('app_path')
    if not os.path.exists(app_path):
        return jsonify({'error': 'App path does not exist!'}), 400
    # Additional validation logic can go here
    return jsonify({'success': 'App path is valid!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python validate_existing_flask_ecommerce_app.py
# Then open: http://127.0.0.1:5000
