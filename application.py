import os

from flask import Flask, render_template, request, flash, session,logging, redirect, url_for
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from books  import Books 
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Books=Books()
usernames=[]
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://postgres:Mariam1985@localhost:5432/booksreview")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/books")
def books():
    return render_template("books.html", books=Books)

@app.route("/book/<string:isbn>/")
def book(isbn):
    return render_template("book.html", isbn=isbn)




@app.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("password")
        confirm=request.form.get("confirm")
        secure_password=sha256_crypt.encrypt(str(password))
        if password == confirm :
            db.execute("INSERT INTO users (name, email, username,password) VALUES (:name, :email, :username,:password)",{"name": name, "email": email, "username": username,"password": secure_password })

            db.commit()

            flash ("You successfully registered", "success")
            return redirect(url_for("login"))
        else:
            flash ("password does not match", "danger")
            return render_template("register.html")

    return render_template("register.html")


@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        username_db= db.execute("SELECT username FROM users WHERE username = :username", {"username": username}).fetchone()
        password_db= db.execute("SELECT password FROM users WHERE username = :username", {"username": username}).fetchone()
        if username_db is None:
            flash ("No username", "danger")
            return render_template("login.html")
        else:
            for password_data in password_db:
                if sha256_crypt.verify(password, password_data):

                    session["log"]=True
                    flash("Congratulation you are now log in", "success")
                    return redirect(url_for("books"))
                else:
                    flash("Wrong pass", "danger")
                    return render_template("login.html")
    return render_template("login.html")

@app.route("/search")
def search():  
    return render_template("search.html") 

@app.route("/logout")
def logout(): 
    session.clear()
    flash ("you log out ", "success") 
    return redirect(url_for("index")) 


if __name__ == "__main__":
    app.secret_key='123'
    app.run(debug=True)