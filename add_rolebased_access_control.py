from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

users = {
    'admin': 'admin_password',
    'user': 'user_password'
}

roles = {
    'admin': 'admin',
    'user': 'user'
}

# Middleware for role-based access control

def role_required(role):
    """Middleware for role-based access control"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or users.get(auth.username) != auth.password:
                return jsonify({'message': 'Authentication required!'}), 401
            if roles.get(auth.username) != role:
                return jsonify({'message': 'Access denied for this role!'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/admin', methods=['GET'])
@role_required('admin')
def admin_route():
    return jsonify({'message': 'Welcome Admin!'}), 200

@app.route('/user', methods=['GET'])
def user_route():
    return jsonify({'message': 'Welcome User!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python add_rolebased_access_control.py
# Then open: http://127.0.0.1:5000