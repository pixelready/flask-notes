from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

# Q: is connect_db a "magic name"?


def connect_db(app):
    """Connect to the DB."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    @classmethod
    def register_user(cls, username, password):
        """Register a new user"""

        hashed = bcrypt.generate_password_hash(password).decode("utf8")

        return cls(username=username, password=hashed)

    @classmethod
    def authenticate_user(cls, username, password):
        """Authenticate a user"""

        current_user = User.query.filter_by(username=username).one_or_none()

        if current_user and bcrypt.check_password_hash(current_user.password, password):

            return current_user

        else:
            return False
