INSERT INTO users (first_name, last_name, street, city, state, country, username, password, age, height_in_cm)
    VALUES ('Jane', 'Doe', '123 Wellness Blvd', 'Fiftyville', 'CA', 'USA', 'Doe_the_Jane', 'hashed_password_here', 30, 165);
    -- inserting a new user


SELECT * FROM measurements
    WHERE user_id = 1 ORDER BY date DESC;
    -- getting an overview on how the meassurements changed over time


SELECT users.id, measurements.date, ROUND((measurements.weight_in_g / 1000) / ((users.height_in_cm / 100) * (users.height_in_cm / 100)), 2) AS BMI
    FROM users
        JOIN measurements ON users.id = measurements.user_id
        WHERE users.id = 1 ORDER BY measurements.date LIMIT 5;
        -- showing the change in BMI over the last 5 measurements

SELECT users.id, measurements.date, ROUND((m.waist_circumference_in_cm / m.hip_circumference_in_cm), 2) AS WHR
    FROM users
        JOIN measurements ON users.id = measurements.user_id
        WHERE users.id = 1
        AND m.waist_circumference_in_cm IS NOT NULL
        AND m.hip_circumference_in_cm IS NOT NULL
        ORDER BY measurements.date LIMIT 5;
        -- showing the change in waist to hips ratio (often more accurate indicator for health than BMI)


SELECT user_id, name, dose, intake_time
    FROM medications
    WHERE currently_prescribed = 'yes';
    -- get a list of medication that should be taken
