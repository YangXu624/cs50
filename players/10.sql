-- In 10.sql, write SQL query to answer a question of your choice. This query should:
-- Make use of AS to rename a column
-- Involve at least condition, using WHERE
-- Sort by at least one column using ORDER BY

SELECT "first_name" AS 'First Name', "last_name" AS 'Last Name' FROM "players"
WHERE "bats" = 'R'
ORDER BY "first_name", "last_name";
