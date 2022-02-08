from enum import unique
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()

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