from flask.ext.wtf import Form
from wtforms import StringField, SubmitField


class TelephoneForm(Form):
    number = StringField('Number', [Length(min=6, max=6), DataRequired()])
    submit = SubmitField('Submit')