-- create a database
CREATE DATABASE project1;

-- select database
\c project1;

-- create a table
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name    VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    visited VARCHAR UNIQUE,
    wishlist VARCHAR UNIQUE
);

-- insert test users
INSERT INTO users (name, password) VALUES ('test1', 'abc123'), ('test2', 'abc123');