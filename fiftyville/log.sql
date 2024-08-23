-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding crimes specific to the street
SELECT * FROM crime_scene_reports
WHERE street = "Humphrey Street";
-- ID: 295, Date: 2023-07-28

-- Interviews specific to the date of crime
SELECT * FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;
-- Drove away within 10 mins of crime
-- Thief withdrew money at Leggett Street on the same day
-- Earliest flight on the next day

SELECT * FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28;
