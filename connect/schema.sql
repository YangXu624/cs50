CREATE TABLE IF NOT EXISTS users (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "username" TEXT,
    "password" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS schools (
    "id" INTEGER,
    "name" TEXT,
    "type" TEXT,
    "location" TEXT,
    "year" INTEGER,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS companies (
    "id" INTEGER,
    "name" TEXT,
    "industry" TEXT,
    "location" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS connections (
    "user_id" INTEGER,
    "connection_id" INTEGER,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("connection_id") REFERENCES "users"("id"),
    PRIMARY KEY("user_id", "connection_id")
);

CREATE TABLE IF NOT EXISTS affiliations (
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start" DATE,
    "end" DATE,
    "type" TEXT,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id"),
    PRIMARY KEY("user_id", "school_id", "start")
);

CREATE TABLE IF NOT EXISTS employment (
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start" DATE,
    "end" DATE,
    "title" TEXT,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "companies"("id"),
    PRIMARY KEY("user_id", "company_id", "start")
);
