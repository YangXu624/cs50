SELECT s."year", s."salary" FROM "players" p
JOIN "salaries" s
    ON p."id" = s."player_id"
WHERE p."first_name" = 'Cal'
    AND p."last_name" = 'Ripken'
ORDER BY s."year" DESC;
