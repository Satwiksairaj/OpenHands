from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/dashboard')
def dashboard_data():
    # Simulating a data fetch delay
    import time
    time.sleep(1)  # Simulating a 1 second delay
    data = {
    'widget_1': [1, 2, 3],
    'widget_2': [4, 5, 6]
}

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python improve_dashboard_performance.py
# Then open: http://127.0.0.1:5000