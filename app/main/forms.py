from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Patient
from wtforms import StringField, TextAreaField, SubmitField





class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class PatientForm(FlaskForm):
    patient = TextAreaField('Patient')
    submit = SubmitField('Submit')


class RecordForm(FlaskForm):
    docter = StringField('Author',validators=[Required()])
    record = TextAreaField('Your Record')
    submit = SubmitField('Submit')
    
