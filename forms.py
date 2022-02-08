from wtforms import StringField,TextAreaField, PasswordField
from flask_wtf import FlaskForm



class RegisterUser(FlaskForm):
    """ Form to register user with username, password, email, first and last name """

    username=StringField("Username")
    password=PasswordField("Password")
    email=StringField("Email")
    first_name=StringField("First Name")
    last_name=StringField("Last Name")