-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding crimes specific to the street. ID: 295, Date: 2023-07-28
SELECT * FROM crime_scene_reports
WHERE street = "Humphrey Street";

-- Interviews specific to the date of crime
SELECT * FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;
