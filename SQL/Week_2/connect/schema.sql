CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS "schools"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "founding_year" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "companies"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "field" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "attended"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id",
    "school_id",
    "started" TEXT NOT NULL,
    "ended" TEXT,
    "graduation_date" TEXT,

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id")
);

CREATE TABLE IF NOT EXISTS "worked"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id",
    "company_id",
    "started" TEXT NOT NULL,
    "ended" TEXT,

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("id")
);
