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
app.config["SQLALCHEMY_DATABASE_URI"]="postgres://zuaxfyzpsshpxt:e2270c239a8629ea70aa2858d25e63a8925ca354da9a6e50b229db2a67781d47@ec2-50-17-178-87.compute-1.amazonaws.com:5432/da0esqb9t1i664"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # print("Creating tables")
    db.create_all()
    file = open("books.csv")
    r = csv.reader(file)
    # print("here")
    for str1 in r:
        details = Books(isbn=str1[0], title=str1[1], author=str1[2], year=int(str1[3]))
        db.session.add(details)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()