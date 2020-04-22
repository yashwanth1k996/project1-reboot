import os

from flask import Flask, session, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *



app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    

    return render_template("home.html")

@app.route("/registration", methods=["GET"])
def registration():
    return render_template("registration.html", message="please register")

@app.route("/elegiblity", methods=["POST", "GET"])
def elegiblity():
    if request.method == 'GET':
        return render_template("home.html")
    name = request.form.get("name")
    password = request.form.get("password")
    if(User.query.get(name) == None):
        # session[name] = []
        details = User(username = name, password = password)
        # session[name].append(name)
        db.session.add(details)
        db.session.commit()
        return render_template("success.html", message = "Successfully Registered")
    else:
        return render_template("login.html", message= "please login, you have already registered")

@app.route("/sendtologin")
def sendtologin():
    return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template("home.html")
    name = request.form.get("name")
    password = request.form.get("password")
    if(User.query.get(name) != None):
        details = User.query.get(name)
        if(password == details.password):
            return render_template("success.html", message = name)
        else:
            return render_template("login.html", message = "incorrect password")
    else:
        return render_template("registration.html", message="you haven't registered please register first")


@app.route("/admin")
def admin():
    valid_users = User.query.all()
    return render_template("admin.html", users = valid_users)

def main():
    db.create_all()
    print("tables created")
    

if __name__ == '__main__':
    with app.app_context():
        main()
    