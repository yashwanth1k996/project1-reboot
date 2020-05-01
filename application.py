import os

from flask import Flask, session, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from sqlalchemy import and_
from user import *



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
        return render_template("login.html", message = "Successfully Registered, please login to explore")
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
            session["name"] = name
            return render_template("success.html", message = name)
        else:
            return render_template("login.html", message = "incorrect password")
    else:
        return render_template("registration.html", message="you haven't registered please register first")


@app.route("/admin")
def admin():
    valid_users = User.query.all()
    return render_template("admin.html", users = valid_users)

@app.route("/bookpage/<string:isbn>", methods = ["GET"])
def bookpage(isbn):
    all_book = Books.query.filter(Books.isbn == isbn).first_or_404()
    # print(all_book.isbn, all_book.title, all_book.author, all_book.year, session["username"])
    session["title"] = all_book.title
    username = session["name"]
    reviews = ReviewRecord.query.filter(and_(ReviewRecord.title == all_book.title, ReviewRecord.rating > 1)).all()
    ownreview = ReviewRecord.query.filter(and_(ReviewRecord.title == all_book.title, ReviewRecord.username == username)).all()
    # flag = False
    # if(ReviewRecord.query.filter(and_(ReviewRecord.username == username, ReviewRecord.title == all_book.title)).all() != []):
    #     flag = True
    flag = given_review(username, all_book.title)
    return render_template("bookpage.html", all_book=all_book, reviews=reviews, ownreview=ownreview, username=username, flag=flag)

@app.route("/recordreview", methods=["POST"])
def recordreview():
    rating = request.form.get("review")
    review = request.form.get("comment")
    username = session["name"]
    bookname = session["title"] 
    data = ReviewRecord(username = username, title = bookname, rating = rating, review = review)
    db.session.add(data)
    db.session.commit()
    return True


def main():
    db.create_all()
    print("tables created")
    

if __name__ == '__main__':
    with app.app_context():
        main()

