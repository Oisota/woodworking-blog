from flask import redirect, url_for
from flask_login import login_required

from app.util import render
from app.services.post import save_post
from .forms import PostForm

def posts():
    """Get all posts with snippets"""
    return render('blog/posts.html')

def post(publish_date, title_slug):
    """View single post"""
    return render('blog/post.html')

def archive():
    """Show archive list of posts"""
    return render('blog/archive.html')

@login_required
def edit_post(post_id):
    """Edit a post"""
    return render('blog/edit_post.html')

#@login_required
def new_post():
    """Draft a new post"""
    form = PostForm()

    if form.validate_on_submit():
        save_post(form.data)
        return redirect(url_for('blog.new_post'))

    return render('blog/new_post.html', {
        'form': form,
    })