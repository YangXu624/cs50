SELECT t."name" FROM "players" p
JOIN "performances" r
    ON p."id" = r."player_id"
JOIN "teams" t
    ON r."team_id" = t."id"
WHERE p."first_name" = 'Satchel'
    AND p."last_name" = 'Paige'
GROUP BY t."name";
