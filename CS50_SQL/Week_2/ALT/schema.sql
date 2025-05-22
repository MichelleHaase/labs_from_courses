CREATE TABLE IF NOT EXISTS "passengers"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS "check-ins"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "passenger_id",
    "flight_id",
    "timestamp" DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY ("flight_id") REFERENCES "flights"("id")
);

CREATE TABLE IF NOT EXISTS "airlines"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT NOT NULL CHECK("concurse" IN ('A','B','C','D','E','F','T'))
);

CREATE TABLE IF NOT EXISTS "flights"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "number" NUMERIC NOT NULL,
    "airline_id",
    "depature_airport_id",
    "arival_airport_id",
    "depature_time" TEXT NOT NULL,
    "arival_time" TEXT NOT NULL,
    FOREIGN KEY ("airline_id") REFERENCES "airlines"("id"),
    FOREIGN KEY ("depature_airport_id") REFERENCES "airports"("id"),
    FOREIGN KEY ("arival_airport_id") REFERENCES "airports"("id")
);


CREATE TABLE IF NOT EXISTS "airports"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "full_name" TEXT NOT NULL UNIQUE,
    "city" TEXT NOT NULL,
    "abbrv" TEXT NOT NULL UNIQUE
);
