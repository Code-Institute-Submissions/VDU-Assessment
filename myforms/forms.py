from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,\
     TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Optional

class Add_CheckForm(FlaskForm):

    image = StringField('Workstation Image', validators=[Optional()])