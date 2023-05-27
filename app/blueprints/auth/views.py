from flask import redirect, url_for

from app.util import render
from .forms import LoginForm

def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('core.home'))
    render('auth/login.html', {
        'form': form
    })

def logout():
    pass

def register():
    pass

def reset():
    pass