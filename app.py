


from crypt import methods
from operator import methodcaller
from flask import Flask, render_template, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User

# Q: is __name__ also a magic name?
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///notes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# TODO: move to .env
app.config["SECRET_KEY"]= "shhhhhh don't tell"
app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)

# --------------

@app.get("/")
def homepage():


# User routes below

@app.route("/register", methods=['GET','POST'])
def register():

    # TODO: form template and html


    return render_template("XYZ.html", form=form)

@app.route("/login", methods=['GET','POST'])
def login():

@app.get("/secret")
def display():

    return "You made it!"