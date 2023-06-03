from datetime import datetime
from flask import redirect, url_for
from flask_login import login_required
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

from app.util import render
from app.services.post import save_post, get_all_posts, get_one_post, get_post_by_id, update_post
from .forms import PostForm

def posts():
    """Get all posts with snippets"""
    posts = get_all_posts()
    return render('blog/posts.html', {
        'posts': posts,
    })

def post(year, month, day, title_slug):
    """View single post"""
    year = int(year)
    month = int(month)
    day = int(day)
    publish_date = datetime(year, month, day)
    post = get_one_post(publish_date, title_slug)
    content = markdown.markdown(post['body'], extensions=['markdown.extensions.fenced_code', CodeHiliteExtension()])
    return render('blog/post.html', {
        'post': post,
        'content': content
    })

def archive():
    """Show archive list of posts"""
    return render('blog/archive.html')

#@login_required
def edit_post(post_id):
    """Edit a post"""
    form = PostForm()
    if form.validate_on_submit():
        update_post(post_id, form.data)
        return redirect(url_for('blog.edit_post', post_id=post_id))

    post = get_post_by_id(post_id)
    form.process(
        title=post['title'],
        publish_date=datetime.fromtimestamp(post['publish_date']),
        content=post['body'],
    )
    print(post['title'])
    print(form.data)
    return render('blog/edit_post.html', {
        'post': post,
        'form': form
    })

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