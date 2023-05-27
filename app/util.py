from flask import render_template

def render(template: str, data: dict):
    """Simple wrapper for render template to make it more how I like"""
    return render_template(template, **data)