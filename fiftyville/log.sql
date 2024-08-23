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

-- Using interview 3
SELECT *
FROM flights
WHERE year = 2023 AND month = 7 AND day = 29
ORDER BY hour
LIMIT 1;
