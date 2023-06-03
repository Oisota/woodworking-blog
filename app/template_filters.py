"""Custom jinja template filters"""

from datetime import datetime

def register_filters(app):
    app.jinja_env.filters['date_format'] = date_format

def date_format(s):
    """Format timestamp to readable date"""
    ts = int(s)
    dt = datetime.fromtimestamp(ts)
    return dt.strftime('%B %d, %Y')
