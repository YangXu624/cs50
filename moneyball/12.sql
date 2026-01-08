SELECT "first_name", "last_name"
FROM "players"
WHERE "id" IN (
    -- Subquery 1: Top 10 least expensive per hit
    SELECT p."id"
    FROM "players" p
    JOIN "salaries" s ON p."id" = s."player_id"
    JOIN "performances" r ON p."id" = r."player_id" AND s."year" = r."year"
    WHERE s."year" = 2001 AND r."H" > 0
    ORDER BY (s."salary" / r."H") ASC
    LIMIT 10
)
INTERSECT
SELECT "first_name", "last_name"
FROM "players"
WHERE "id" IN (
    -- Subquery 2: Top 10 least expensive per RBI
    SELECT p."id"
    FROM "players" p
    JOIN "salaries" s ON p."id" = s."player_id"
    JOIN "performances" r ON p."id" = r."player_id" AND s."year" = r."year"
    WHERE s."year" = 2001 AND r."RBI" > 0
    ORDER BY (s."salary" / r."RBI") ASC
    LIMIT 10
)
ORDER BY "last_name", "first_name";
