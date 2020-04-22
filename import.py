import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://teylbeslojzmbb:4d02fe2395dc1b53ad0d61d1fb47f90545285b32a5a718c2e1ff9376e6fe3b47@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d1jrno0m78ogcj"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy()
db.init_app(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # db.create_all()
    details = User(username = "Yash", password = "password")
    print("part1 done")
    db.session.add(details)
    print("part2 donr")
    db.session.commit()
    print("part3 done")