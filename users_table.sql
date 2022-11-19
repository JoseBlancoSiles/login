-- SQLite Creates table for our registants, USERNAME must be UNIQUE in order to prevent multiple registrations.

DROP TABLE IF EXISTS users;
CREATE TABLE users(id INTEGER, username TEXT NOT NULL UNIQUE, email TEXT NOT NULL, password TEXT NOT NULL, PRIMARY KEY(id));