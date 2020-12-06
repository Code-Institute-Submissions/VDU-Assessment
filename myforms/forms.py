from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField,\
validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo, Optional

class RegistrationForm(FlaskForm):
    fname = StringField('Firstname', [validators.length(min=2, max=15)])
    username = StringField('Username', [validators.length(min=3, max=15)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.length(min=3, max=15)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

class Add_CheckForm(FlaskForm):

    image = StringField('Workstation Image', validators=[Optional()])