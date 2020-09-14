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


class RegisterForm(Form):
    name=StringField('Name', [validators.length(min=1, max=50)])
    email=StringField('Email', [validators.length(min=1, max=50)])
    username=StringField('Username', [validators.length(min=1, max=25)])
    password=PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message= 'Password do not match')
    ])
    confirm= PasswordField("Confirm Password")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form =RegisterForm(request.form)
    if request.method== 'POST' and form.validate():
        name =form.name.data
        email=form.email.data
        username=form.username.data
        password=sha256_crypt.encrypt(str(form.password.data))
        db.execute("INSERT INTO users (name, email, username, password) VALUES (:name, :email, :username,:password)",
            {"name": name, "email": email, "username":username, "password": password })
        db.commit()
        flash ('You are now regirter', 'Success')
        redirect(url_for('index'))

        return render_template("register.html")
    return render_template("register.html", form=form)