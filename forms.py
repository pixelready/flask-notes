from wtforms import StringField, TextAreaField, PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import email_validator


class RegisterUser(FlaskForm):
    """Form to register user with username, password, email, first and last name"""

    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired()])
    first_name = StringField("First Name", validators=[validators.DataRequired()])
    last_name = StringField("Last Name", validators=[validators.DataRequired()])
