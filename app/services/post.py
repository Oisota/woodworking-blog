from slugify import slugify
from datetime import datetime

from app.database import get_db, query_db

def get_all_posts():
    db = get_db()
    query = """
    select id, title, title_slug, publish_date, body
    from post;
    """
    result = query_db(query)
    return result

def get_one_post(publish_date, title_slug):
    db = get_db()
    query = """
    select id, title, title_slug, publish_date, body
    from post
    where publish_date = ? and title_slug = ?;
    """
    result = query_db(query, (publish_date, title_slug), one=True)
    return result

def get_post_by_id(post_id):
    db = get_db()
    query = """
    select id, title, title_slug, publish_date, body
    from post
    where id = ?;
    """
    result = query_db(query, (post_id,), one=True)
    return result

def update_post(post_id, post_data):
    """Save post to DB"""
    db = get_db()
    query = """
    update post set
        title = :title,
        title_slug = :slug,
        publish_date = :date,
        body = :body
    where id = :post_id;
    """

    publish_date = post_data['publish_date']
    date = datetime(
        year=publish_date.year,
        month=publish_date.month,
        day=publish_date.day
    )
    params = {
        'post_id': post_id,
        'title': post_data['title'],
        'slug': slugify(post_data['title']),
        'date': round(date.timestamp()),
        'body': post_data['content'],
    }

    db.execute(query, params)
    db.commit()

def save_post(post_data):
    """Save post to DB"""
    db = get_db()
    query = """
    insert into post (
        title,
        title_slug,
        publish_date,
        body
    ) values (
        :title, :slug, :date, :body
    );
    """

    publish_date = post_data['publish_date']
    date = datetime(
        year=publish_date.year,
        month=publish_date.month,
        day=publish_date.day
    )
    params = {
        'title': post_data['title'],
        'slug': slugify(post_data['title']),
        'date': round(date.timestamp()),
        'body': post_data['content'],
    }

    db.execute(query, params)
    db.commit()