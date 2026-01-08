SELECT p."first_name", p."last_name", s."salary" / r."H" AS 'dollars per hit'
FROM "players" p
JOIN "performances" r ON p."id" = r."player_id"
JOIN "salaries" s ON p."id" = s."player_id"
    AND r."year" = s."year"
WHERE r."year" = 2001
AND r."H" > 0
ORDER BY "dollars per hit",
    p."first_name",
    p."last_name"
LIMIT 10;
