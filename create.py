import os
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
# postgres://teylbeslojzmbb:4d02fe2395dc1b53ad0d61d1fb47f90545285b32a5a718c2e1ff9376e6fe3b47@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d1jrno0m78ogcj

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    print("Creating tables")
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
