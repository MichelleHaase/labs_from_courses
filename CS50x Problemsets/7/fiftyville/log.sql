-- Keep a log of any SQL queries you execute as you solve the mystery.
-- get the description of the theft
SELECT description FROM crime_scene_reports
    WHERE street = 'Humphrey Street'
    AND day = 28
    AND month = 7
    AND year = 2024;
--      time 10:15; at Humphrey Street bakery; 3 witnesses all mention bakery; litering 16:36
-- get witness accounts
SELECT transcript FROM interviews
    WHERE day = 28
    AND month = 7
    AND year = 2024;
--      1. within 10 min, car in bakery parkinglot --> footage bakery_security_logs Plate and
--      2. sometime before 10:15 ATM on Leggett Street withdrew money -> account number/ amount -> acountnumber bank_accounts person_id
--      3. overheard call <1 min earlirst flight from fiftyville on 29th july 2024 other person bought ticket -> phone_calls time 10:15 -10:25 duration< 1 get caller reciever
-- check info witness 3
SELECT * FROM phone_calls
    WHERE year = 2024
    AND month = 7
    AND day = 28
    AND duration < 60;
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2024 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2024 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2024 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2024 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2024 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2024 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2024 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+
*/
-- get info second witness
SELECT * FROM atm_transactions
    WHERE atm_location = 'Leggett Street'
    AND year = 2024
    AND month = 7
    AND day = 28
    AND transaction_type = 'withdraw';
--      to many entries
-- first witness
SELECT * FROM bakery_security_logs
    WHERE year = 2024
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute >=15
    AND minute <= 25
    AND activity = 'exit';

-- get potential passport number
 -- airport id
 SELECT * FROM airports
    WHERE city = 'Fiftyville';
-- id = 8
 --  get flight
SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2024 AND month = 7 AND day = 29 ORDER BY hour, minute;
-- first flight destination id = 4 flight id = 36

-- get destination airport
SELECT * FROM airports WHERE id = 4;
-- --> destination New York City

-- get passengers from flight 36
SELECT passport_number FROM passengers WHERE flight_id = 36;

-- get the thief

SELECT name FROM people
    WHERE phone_number IN
        (SELECT caller FROM phone_calls
            WHERE year = 2024
            AND month = 7
            AND day = 28
            AND duration < 60)
    AND passport_number IN
        (SELECT passport_number FROM passengers
            WHERE flight_id =
                (SELECT id FROM flights
                    WHERE origin_airport_id =
                        ( SELECT id FROM airports
                            WHERE city = 'Fiftyville')
                        AND year = 2024
                        AND month = 7
                        AND day = 29
                        ORDER BY hour, minute))
    AND license_plate IN
        (SELECT license_plate FROM bakery_security_logs
            WHERE year = 2024
            AND month = 7
            AND day = 28
            AND hour = 10
            AND minute >=15
            AND minute <= 25
            AND activity = 'exit')
    AND id IN
        (SELECT person_id FROM bank_accounts
            WHERE account_number IN
                ( SELECT account_number FROM atm_transactions
                    WHERE year = 2024
                    AND month = 7
                    AND day= 28
                    AND transaction_type = 'withdraw'));
-- colprit is BRUCE

-- Bruces Number -> his partner reciever
SELECT people.name, phone_calls.caller , phone_calls.receiver FROM people
    JOIN phone_calls
    ON people.phone_number = phone_calls.caller
        WHERE phone_number IN

            (SELECT caller FROM phone_calls
                WHERE year = 2024
                AND month = 7
                AND day = 28
                AND duration < 60)
        AND passport_number IN

            (SELECT passport_number FROM passengers
                WHERE flight_id =

                (SELECT id FROM flights
                    WHERE origin_airport_id =

                    ( SELECT id FROM airports
                        WHERE city = 'Fiftyville')

                AND year = 2024
                AND month = 7
                AND day = 29
                ORDER BY hour, minute))
        AND license_plate IN

            (SELECT license_plate FROM bakery_security_logs
                WHERE year = 2024
                AND month = 7
                AND day = 28
                AND hour = 10
                AND minute >=15
                AND minute <= 25
                AND activity = 'exit')
        AND people.id IN

            (SELECT person_id FROM bank_accounts
                WHERE account_number IN

                    ( SELECT account_number FROM atm_transactions
                        WHERE year = 2024
                        AND month = 7
                        AND day= 28
                        AND transaction_type = 'withdraw'))
        AND phone_calls.year = 2024
        AND phone_calls.month = 7
        AND phone_calls.day = 28
        AND phone_calls.duration < 60;
-- Bruces partners number (375) 555-8161
SELECT name FROM people
    JOIN phone_calls
    ON people.phone_number = phone_calls.caller
        WHERE caller = '(375) 555-8161';
-- accomlice is Robin
