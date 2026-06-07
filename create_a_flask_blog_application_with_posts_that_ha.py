"""
create_a_flask_blog_application_with_posts_that_ha.py
=============
A Flask blog application with posts that have title, content, and date.

Usage:
    python create_a_flask_blog_application_with_posts_that_ha.py

Author: Autonomous Agent
"""
from typing import Any, Dict, List, Optional, Tuple
from flask import Flask, request, jsonify, render_template
from datetime import datetime

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

# =============================================================================
# MODELS
# =============================================================================
class Post:
    """Model for blog posts."""

    def __init__(self, title: str, content: str, date: Optional[datetime] = None) -> None:
        self.title = title
        self.content = content
        self.date = date or datetime.now()
    def to_dict(self) -> Dict[str, Any]:
        return {'title': self.title, 'content': self.content, 'date': self.date.strftime('%Y-%m-%d %H:%M:%S')}

# Database configuration using SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Post model for database storage
class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
def create_db():
    with app.app_context():
        db.create_all()
posts: List[Post] = []

# =============================================================================
# ROUTES
# =============================================================================
@app.route('/')
def index() -> Tuple[Any, int]:
    """Home page that lists all posts."""
    return render_template('index.html', posts=[post.to_dict() for post in posts])

@app.route('/post/<int:post_id>')
def view_post(post_id: int) -> Tuple[Any, int]:
    """View a single post."""
    if 0 <= post_id < len(posts):
        return render_template('view_post.html', post=posts[post_id].to_dict())
    return jsonify({'error': 'Post not found'}), 404

@app.route('/post/new', methods=['GET', 'POST'])
def new_post() -> Tuple[Any, int]:
    """Create a new post."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title, content)
        posts.append(post)
        return jsonify({'message': 'Post created!', 'post': post.to_dict()}), 201
    return render_template('new_post.html')

# =============================================================================
# ERROR HANDLERS
# =============================================================================
@app.errorhandler(404)
def not_found(error) -> Tuple[Any, int]:
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error) -> Tuple[Any, int]:
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# =============================================================================
# ENTRY POINT
# =============================================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_blog_application_with_posts_that_ha.py
# Then open: http://127.0.0.1:5000