CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,  
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL
  
);


CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,  
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    register date TIMESTAMP
);