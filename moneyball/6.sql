SELECT t."name", SUM(r."H") AS 'total hits'
FROM "teams" t
JOIN "performances" r
    ON t."id" = r."team_id"
WHERE r."year" = 2001
GROUP BY t."id"
ORDER BY "total hits" DESC
LIMIT 5;
