import os

from flask import Flask, render_template, request, flash, session,logging
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from books  import Books 
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Books=Books()

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

@app.route("/books")
def books():
    return render_template("books.html", books=Books)

@app.route("/book/<string:isbn>/")
def book(isbn):
    return render_template("book.html", isbn=isbn)




@app.route("/register", methods=['GET', 'POST'])
def register():

    return render_template("register.html")

@app.route("/login")
def login():
    
    return render_template("login.html")