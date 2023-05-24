from flask import render_template
from flask_login import login_required

def posts():
    """Get all posts with snippets"""

def post(publish_date, title_slug):
    """View single post"""

def archive():
    """Show archive list of posts"""

@login_required
def edit_post(post_id):
    """Edit a post"""

#@login_required
def new_post():
    """Draft a new post"""
    return render_template('new_post.html')