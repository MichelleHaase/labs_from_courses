
.import --csv meteorites.csv temp_table

CREATE TABLE IF NOT EXISTS meteorites(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "class" TEXT,
    "mass" REAL DEFAULT NULL,
    "discovery" TEXT CHECK("discovery" IN ('Fell', 'Found')),
    "year" INTEGER DEFAULT NULL,
    "lat" REAL DEFAULT NULL,
    "long" REAL DEFAULT NULL
);

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", ROUND("mass",2), "discovery", "year", ROUND("lat",2), ROUND("long",2) FROM "temp_table" WHERE "nametype" NOT LIKE 'Relict' ORDER BY "year", "name";

UPDATE meteorites SET mass = NULL WHERE mass = 0.0 OR mass = '';
UPDATE meteorites SET year = NULL WHERE year = 0 OR year = '';
UPDATE meteorites SET lat = NULL WHERE lat = 0.0 OR lat = '';
UPDATE meteorites SET long = NULL WHERE long = 0.0 OR long = '';

DROP TABLE temp_table;
