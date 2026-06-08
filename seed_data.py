from extensions import db
from models import Post, Comment
from datetime import datetime

# Sample data
posts = [
    Post(title='First Post', slug='first-post', content='Lorem ipsum dolor sit amet...', author='John Doe', category='General', published_at=datetime.now(), is_published=True),
    Post(title='Second Post', slug='second-post', content='Another post content...', author='Jane Doe', category='Technology', published_at=datetime.now(), is_published=True),
    Post(title='Third Post', slug='third-post', content='More interesting content...', author='Jim Bean', category='Lifestyle', published_at=datetime.now(), is_published=True),
    Post(title='Draft One', slug='draft-one', content='This is a draft...', author='Jack Daniels', category='Drafts', is_published=False),
    Post(title='Draft Two', slug='draft-two', content='Second draft content...', author='Jill Valentine', category='Drafts', is_published=False)
]

comments = [
    Comment(post_id=1, author_name='Alice', content='Great post!', created_at=datetime.now()),
    Comment(post_id=1, author_name='Bob', content='Thanks for this information.', created_at=datetime.now()),
    Comment(post_id=2, author_name='Charlie', content='Interesting read.', created_at=datetime.now()),
    Comment(post_id=2, author_name='Dave', content='I learned something new.', created_at=datetime.now()),
    Comment(post_id=3, author_name='Eve', content='Will share this!', created_at=datetime.now()),
    Comment(post_id=4, author_name='Frank', content='Looking forward to the update...', created_at=datetime.now()),
    Comment(post_id=4, author_name='Grace', content='Can’t wait to read more.', created_at=datetime.now()),
    Comment(post_id=5, author_name='Heidi', content='Good draft.', created_at=datetime.now()),
]

def seed_database():
    db.session.add_all(posts)
    db.session.add_all(comments)
    db.session.commit()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        seed_database()
        print('Database seeded!')
