CREATE TABLE IF NOT EXISTS "ingredients"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE,
    "stock" NUMERIC, -- amount that is in stock
    "stock_unit" TEXT NOT NULL, -- unit like grams pounds
    "price_per_stock_unit" NUMERIC NOT NULL,
    "purchase_date" TEXT
);

CREATE TABLE IF NOT EXISTS "donuts"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE,
    "gluten" INTEGER NOT NULL CHECK("gluten" IN (0,1)),
    "price" REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS "recepies"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "ingredient_id",
    "donuts_id",

    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients"("id"),
    FOREIGN KEY ("donuts_id") REFERENCES "donuts"("id")
);

CREATE TABLE IF NOT EXISTS "orders"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "donut_id",
    "costumer_id",

    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("costumer_id") REFERENCES "costumers"("id")
);

CREATE TABLE IF NOT EXISTS "costumers"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL
);
