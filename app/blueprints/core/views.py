from flask import render_template

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')