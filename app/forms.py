from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class CommentForm(Form):
    username = StringField('username', validators=[DataRequired()])
    comment = StringField('comment', validators=[DataRequired()],widget=TextArea())