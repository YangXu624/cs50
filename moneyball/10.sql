SELECT p."first_name", p."last_name", s."salary", r."year", r."HR" FROM "players" p
JOIN "performances" r ON p."id" = r."player_id"
JOIN "salaries" s ON p."id" = s."player_id"
    AND r."year" = s."year"
ORDER BY p."id",
    s."year" DESC,
    r."HR" DESC,
    s."salary" DESC;
