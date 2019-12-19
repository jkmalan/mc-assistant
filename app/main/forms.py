from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired()
    ])
    password = PasswordField('Password', validators=[
        InputRequired()
    ])
    remember = BooleanField('Remember')
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired()
    ])
    email = StringField('Email', validators=[
        InputRequired(),
        Email()
    ])
    phone = StringField('Phone', validators=[
        InputRequired()
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8, message='The password must be at least 8 characters')
    ])
    password_verify = PasswordField('Retype Password', validators=[
        InputRequired(),
        EqualTo('password', message='The passwords must be the same')
    ])
    firstname = StringField('First Name', validators=[
        InputRequired()
    ])
    lastname = StringField('Last Name', validators=[
        InputRequired()
    ])
    submit = SubmitField('Submit')
