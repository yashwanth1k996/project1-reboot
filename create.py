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
app.config["SQLALCHEMY_DATABASE_URI"]="postgres://zuaxfyzpsshpxt:e2270c239a8629ea70aa2858d25e63a8925ca354da9a6e50b229db2a67781d47@ec2-50-17-178-87.compute-1.amazonaws.com:5432/da0esqb9t1i664"
# postgres://teylbeslojzmbb:4d02fe2395dc1b53ad0d61d1fb47f90545285b32a5a718c2e1ff9376e6fe3b47@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d1jrno0m78ogcj

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    print("Creating tables")
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()