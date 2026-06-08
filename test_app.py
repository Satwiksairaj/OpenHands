import pytest
from flask import url_for
from app import app as flask_app
from models import db, Post

@pytest.fixture
def app():
    flask_app.config.from_mapping(SQLALCHEMY_DATABASE_URI='sqlite:///:memory:', TESTING=True)
    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def create_post(client, title, slug, content, author, category):
    client.get('/admin/posts', follow_redirects=True)  # Ensure session context loaded
    return client.post(url_for('create_post'), data={
        'title': title,
        'slug': slug,
        'content': content,
        'author': author,
        'category': category
    }, follow_redirects=True)


def test_create_post(client):
    response = create_post(client, 'Testing Post', 'testing-post', 'Test content...', 'Tester', 'Testing')
    with client.session_transaction() as session:
        assert ('success', 'New post created!') in session['_flashes']
    assert Post.query.filter_by(slug='testing-post').first() is not None


def test_toggle_publish(client):
    create_post(client, 'Test Toggle', 'test-toggle', 'Content', 'Author', 'Category')
    post = Post.query.filter_by(slug='test-toggle').first()
    response = client.post(url_for('toggle_publish_status', id=post.id), follow_redirects=True)
    with client.session_transaction() as session:
        assert ('success', 'Post publication status toggled!') in session['_flashes']


def test_submit_comment(client):
    create_post(client, 'Test Comment', 'test-comment', 'Content', 'Author', 'Category')
    response = client.post(url_for('view_post', slug='test-comment'), data={
        'author': 'Commenter',
        'content': 'This is a comment.'
    }, follow_redirects=True)
    with client.session_transaction() as session:
        assert ('success', 'Your comment has been posted!') in session['_flashes']


def test_api_stats(client):
    create_post(client, 'Test Stats', 'test-stats', 'Content', 'Author', 'Category')
    response = client.get(url_for('api_stats'))
    assert response.status_code == 200
    data = response.get_json()
    assert 'total_posts' in data
    assert 'comments_per_post' in data
    assert 'top_commented_posts' in data
    assert 'published_vs_draft_counts' in data
