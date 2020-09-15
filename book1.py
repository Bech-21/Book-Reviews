import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine =create_engine("postgresql://postgres:Mariam1985@localhost:5432/booksreview")
db = scoped_session(sessionmaker(bind=engine))

def main():
    username= input()
    username_db= db.execute("SELECT username FROM users WHERE username = :username", {"username": username}).fetchone()
    password_db= db.execute("SELECT password FROM users WHERE username = :username", {"username": username}).fetchone()
    print(username_db)
    print(f"Flight {username_db}: {password_db}  minutes.")



if __name__ == "__main__":
    main()
