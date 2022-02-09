from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms import validators


class RegisterUser(FlaskForm):
    """Form to register user with username, password, email, first and last name"""

    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired()])
    first_name = StringField("First Name", validators=[validators.DataRequired()])
    last_name = StringField("Last Name", validators=[validators.DataRequired()])


class LoginUser(FlaskForm):
    """Form to login user with username, password"""

    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])


class OnlyCSRF(FlaskForm):
    """Pass a CSRF token to an empty form"""
