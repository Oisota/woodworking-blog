from flask_wtf import FlaskForm
from wtforms import StringField, DateField, HiddenField

class PostForm(FlaskForm):
    title = StringField('Title')
    publish_date = DateField('Date')
    content = HiddenField('Content')
