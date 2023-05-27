from slugify import slugify
from datetime import datetime

from app.database import get_db

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
    )
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