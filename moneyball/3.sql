SELECT r."year", r."HR" FROM "players" p
JOIN "performances" r
    ON p."id" = r."player_id"
WHERE p."first_name" = 'Ken'
    AND p."last_name" = 'Griffey'
    AND p."birth_year" = 1969
ORDER BY r."year" DESC;
