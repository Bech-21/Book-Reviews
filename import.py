import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine =create_engine("postgresql://postgres:Mariam1985@localhost:5432/booksreview")
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        header=next(reader)
        if header != None:
            for isbn, title, author,year in reader:
                db.execute("INSERT INTO books (isbn, title, author,year) VALUES (:isbn, :title, :author,:year)",
                    {"isbn": isbn, "title": title, "author": author,"year": year })
                print(f"Added flight from {isbn} to {title} lasting {author} minutes,{year}.")
            db.commit()

if __name__ == "__main__":
    main()
