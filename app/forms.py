from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class TelephoneForm(Form):
    area_code = StringField('Area Code')
    central_office_code = StringField('Central Office Code')
    submit = SubmitField('Submit')