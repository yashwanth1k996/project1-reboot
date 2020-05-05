import os
import csv
from flask import request
from flask import render_template
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, String
from models import *
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://yainmriqptbdia:ef9eb65b36e26462fab4fa3190ea7982f65a5b450e7be9789b4ac2f507b8f634@ec2-54-81-37-115.compute-1.amazonaws.com:5432/d226orf1s2l1ac"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # print("Creating tables")
    db.create_all()
    file = open("books.csv")
    r = csv.reader(file)
    # print("here")
    for str1 in r:
        details = Books(isbn=str1[0], title=str1[1], author=str1[2], year=str1[3])
        db.session.add(details)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
