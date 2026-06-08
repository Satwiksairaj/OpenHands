from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from extensions import db
from models import Post, Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)

@app.route('/')
def home():
    from models import Post
    posts = Post.query.filter_by(is_published=True).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<slug>', methods=['GET', 'POST'])
def view_post(slug):
    from models import Post, Comment
    post = Post.query.filter_by(slug=slug).first_or_404()
    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        comment = Comment(post_id=post.id, author_name=author, content=content)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted!', 'success')
        return redirect(url_for('view_post', slug=slug))
    return render_template('post.html', post=post)

@app.route('/admin/posts')
def manage_posts():
    from models import Post
    posts = Post.query.all()
    return render_template('admin_posts.html', posts=posts)

@app.route('/admin/posts/new', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        slug = request.form['slug']
        content = request.form['content']
        author = request.form['author']
        category = request.form['category']
        post = Post(title=title, slug=slug, content=content, author=author, category=category)
        db.session.add(post)
        db.session.commit()
        flash('New post created!', 'success')
        return redirect(url_for('manage_posts'))
    return render_template('new_post.html')

@app.route('/admin/posts/<int:id>/publish', methods=['POST'])
def toggle_publish_status(id):
    post = Post.query.get_or_404(id)
    post.is_published = not post.is_published
    db.session.commit()
    flash('Post publication status toggled!', 'success')
    return redirect(url_for('manage_posts'))

@app.route('/api/stats')
def api_stats():
    total_posts = Post.query.count()
    published_posts = Post.query.filter_by(is_published=True).count()
    draft_posts = total_posts - published_posts
    comments_per_post = {post.id: len(post.comments) for post in Post.query.all()}
    top_commented_posts = sorted(comments_per_post.items(), key=lambda item: item[1], reverse=True)[:3]
    return jsonify({
        'total_posts': total_posts,
        'published_vs_draft_counts': {'published': published_posts, 'draft': draft_posts},
        'comments_per_post': comments_per_post,
        'top_commented_posts': top_commented_posts
    })

if __name__ == '__main__':
    app.run(debug=True)