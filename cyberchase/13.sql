-- In 13.sql, write a SQL query to explore a question of your choice. This query should:
-- Involve at least one condition, using WHERE with AND or OR

SELECT ROUND(AVG("season"), 2) FROM "episodes"
WHERE (
    ("air_date" BETWEEN '2002-01-01' AND '2003-12-31')
    OR "air_date" LIKE '2007%'
);
