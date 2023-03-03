from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserSignupForm(FlaskForm):
    #email, password, first_name, last_name
    email = StringField('Email', validators = [DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class UserLoginForm(FlaskForm):
    #email, password, first_name, last_name
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class BlockForm(FlaskForm):
    block = StringField('Block', validators = [DataRequired()])
    submit_button = SubmitField('Submit')