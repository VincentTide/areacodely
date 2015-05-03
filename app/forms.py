from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class TelephoneForm(Form):
    number = StringField('Number')
    submit = SubmitField('Submit')