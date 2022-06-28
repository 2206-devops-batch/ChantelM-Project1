from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
# python classes are converted to html using flask_wtf

class SignupForm(FlaskForm):
    username = StringField('Username',
            validators=[DataRequired(), Length(min=5, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1)])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=1), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username',
            validators=[DataRequired(), Length(min=5, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Login')
