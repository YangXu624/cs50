-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding crimes specific to the street
SELECT * FROM crime_scene_reports
WHERE street = "Humphrey Street";
-- ID: 295, Date: 2023-07-28, 10.15 am

-- Interviews specific to the date of crime
SELECT * FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;
-- Drove away within 10 mins of crime
-- Thief withdrew money at Leggett Street on the same day
-- Earliest flight on the next day

-- Using interview 1
SELECT * FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25;
-- List of potential liscence plates within 10 mins time frame

-- Using interview 2
SELECT *
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE atm_location = "Leggett Street"
      AND year = 2023
      AND month = 7
      AND day = 28
      AND transaction_type = "withdraw"
);
-- List of person_id that fit description of interview 2

-- Using above info (from interview 2)
SELECT * FROM phone_calls
WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;

-- Using interview 3
SELECT *
FROM passengers
WHERE flight_id IN (
    SELECT id
    FROM flights
    WHERE year = 2023
      AND month = 7
      AND day = 29
    ORDER BY hour
    LIMIT 1
);
-- List of passport numbers

-- Putting everything together
SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2023
      AND month = 7
      AND day = 28
      AND hour = 10
      AND minute > 15
      AND minute < 25
)
AND passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE year = 2023
          AND month = 7
          AND day = 29
        ORDER BY hour
        LIMIT 1
    )
AND phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
    )
AND id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE atm_location = "Leggett Street"
        AND year = 2023
        AND month = 7
        AND day = 28
        AND transaction_type = "withdraw"
        )
    )
);

-- City he escaped to
SELECT city
FROM airports
WHERE id IN (
    SELECT destination_airport_id
    FROM flights
    WHERE year = 2023
        AND month = 7
        AND day = 29
    ORDER BY hour
    LIMIT 1
);

-- Accomplice
SELECT people.name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28
AND phone_calls.duration <= 60 AND phone_calls.caller = '(367) 555-5533';
