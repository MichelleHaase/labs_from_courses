CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL ,
    "last_name" TEXT NOT NULL ,
    "street" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT, -- can be null since not all countries require states in addresses
    "country" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL, -- should only be saved as Hash
    "age" INTEGER NOT NULL,
    "height_in_cm" INTEGER NOT NULL

);

CREATE TABLE IF NOT EXISTS "measurements"( -- can be used to query different health indicies like BMI or waist to hips
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "weight_in_g" INTEGER NOT NULL,
    "hip_circumference_in_cm" INTEGER,
    "waist_circumference_in_cm" INTEGER,
    "left_arm_circumference_in_cm" INTEGER,
    "chest_circumference_in_cm" INTEGER,
    "left_thight_circumference_in_cm" INTEGER,
    "left_calf_circumference_in_cm" INTEGER,
    "date" DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY ("user_id") REFERENCES "users"("id")
);

CREATE TABLE IF NOT EXISTS "metrics"( -- most important blood meassurements
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "doctor_id" INTEGER NOT NULL,
    "systolic_BP" NUMERIC,
    "Dyostolic_BP" NUMERIC,
    "longterm_glucose" NUMERIC,
    "LDL_cholesterol" NUMERIC,
    "HDL_cholesterol" NUMERIC,
    "Triglycerides" NUMERIC,
    "Complete_blood_count" NUMERIC,
    "Thyroid_stimulating_hormone" NUMERIC,
    "date" DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("doctor_id") REFERENCES "doctors"("id")
);

CREATE TABLE IF NOT EXISTS "medications"( -- overview over prescrited medications
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "doctor_id" INTEGER NOT NULL,
    "condition_id" INTEGER NOT NULL,
    "metric_id" INTEGER, -- metric that was the indicator for the prescription
    "name" TEXT NOT NULL,
    "dose" TEXT NOT NULL, -- text to allow for different units
    "intake_time" TEXT, -- daytime at which the medication should be taken
    "food_remarks" TEXT,  -- like take with food or after, not to be taken with diary products
    "currently_prescribed" TEXT NOT NULL CHECK(currently_prescribed IN ('yes', 'no')), -- check that the medicatiuon is currently taken
    "archived" DATE, -- date since a medication is no longer taken

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("doctor_id") REFERENCES "doctors"("id"),
    FOREIGN KEY ("condition_id") REFERENCES "conditions"("id"),
    FOREIGN KEY ("metric_id") REFERENCES "metrics"("id")
);

CREATE TABLE IF NOT EXISTS "doctors"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "speciality" TEXT NOT NULL,
    "street" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT,
    "country" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "visits"( -- documentation on doctor visits
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "doctor_id" INTEGER NOT NULL,
    "metrics_id" INTEGER,
    "condition_id" INTEGER,
    "measuremnet_id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "medication_id" INTEGER,
    "newly_prescibed" TEXT NOT NULL CHECK(newly_prescibed IN ('yes', 'no')),
    "date" DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("doctor_id") REFERENCES "doctors"("id"),
    FOREIGN KEY ("metrics_id") REFERENCES "metrics"("id"),
    FOREIGN KEY ("condition_id") REFERENCES "conditions"("id"),
    FOREIGN KEY ("measuremnet_id") REFERENCES "measurements"("id"),
    FOREIGN KEY ("medication_id") REFERENCES "medications"("id")

);

CREATE TABLE IF NOT EXISTS "conditions"( -- overview of conditions and doctors that diagnosed them
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "condition" TEXT NOT NULL,
    "doctor_id" INTEGER, -- doctor who diagnosed condition

    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("doctor_id") REFERENCES "doctors"("id")
);
-- View for condition and medications overview
CREATE VIEW condtion_details AS
SELECT  users.first_name AS 'First Name',
        users.last_name AS 'Last Name',
        conditions.condition AS 'Condition',
        doctors.name AS 'Doctor',
        medications.name AS 'Medication',
        medications.dose AS 'Dose'
FROM users
    JOIN conditions ON users.id = conditions.user_id
    JOIN doctors ON users.id = doctors.user_id
    JOIN medications ON users.id = medications.user_id;

