from flask import Flask, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import OnlyCSRF, RegisterUser, LoginUser
from models import connect_db, db, User

# raise Exception("Hello!")

# Q: is __name__ also a magic name?
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///notes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# TODO: move to .env
app.config["SECRET_KEY"] = "shhhhhh don't tell"
app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# --------------


@app.get("/")
def homepage():
    return redirect("/register")


# User routes below ##########################################################


@app.route("/register", methods=["GET", "POST"])
def register():

    # TODO: form template and html
    form = RegisterUser()

    if form.validate_on_submit():
        # Q: how do we do some fancy decompose footwork for this?
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        new_user = User.register_user(username, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    else:
        return render_template("register_user.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginUser()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if User.authenticate_user(username, password):
            session["user_id"] = username

            return redirect(f"/users/{username}")
        else:
            form.username.errors = ["Bad username / password"]
            return render_template("login_user.html", form=form)

    else:
        return render_template("login_user.html", form=form)


# Old, defunct route
# @app.get("/secret")
# def display_sooper_secret_page():
#     """Let authenticed Users into the secret chamber"""

#     if session.get("user_id"):
#         return render_template("secret.html")
#     else:
#         flash("Nice try, pleb.")
#         return redirect("/")


@app.get("/users/<username>")
def display_user_profile(username):
    """Displays information about current logged in user"""

    current_user = User.query.get(username)
    form = OnlyCSRF()

    if session.get("user_id") == username:

        return render_template(
            "user_profile.html", current_user=current_user, form=form
        )

    elif session.get("user_id") and session.get("user_id") != username:

        redirect_user = session.get("user_id")

        return redirect(f"/users/{redirect_user}")

    else:
        return redirect("/login")


@app.post("/logout")
def logout_current_user():
    """Delete the user from the current session and redirect to homepage"""

    if OnlyCSRF(request.form).validate_on_submit() and session.get("user_id"):
        session.pop("user_id", None)
        return redirect("/")
    else:
        return redirect("/")
