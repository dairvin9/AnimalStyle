from flask_wtf import Form
from wtforms import StringField, BooleanField, ValidationError
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


# validators.length(max=10)]

class CommentForm(Form):
    username = StringField('username', validators=[DataRequired()])
    comment = StringField('comment', validators=[DataRequired()],widget=TextArea())