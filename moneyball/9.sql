SELECT t."name", ROUND(AVG(s."salary"), 2) AS 'average salary'
FROM "teams" t
JOIN "salaries" s
    ON t."id" = s."team_id"
WHERE s."year" = 2001
GROUP BY t."id"
ORDER BY "average salary"
LIMIT 5;
