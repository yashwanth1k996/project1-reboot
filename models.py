from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    user_created_on = db.Column(db.DateTime, nullable = False)

    def __init__(self, username, password, user_created_on=None):
        self.username = username
        self.password = password
        self.user_created_on = datetime.now()

class Books(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author=db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)