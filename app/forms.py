from flask_wtf import Form
from wtforms import StringField, BooleanField, ValidationError
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


def length(min=-1, max=-1):
    message = 'Must be between %d and %d characters long.' % (min, max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)


class CommentForm(Form):
    username = StringField('username', validators=[DataRequired()])
    comment = StringField('comment', validators=[DataRequired()],widget=TextArea())