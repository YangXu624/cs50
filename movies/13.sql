SELECT p1.name
FROM people p1
JOIN stars s1 ON p1.id = s1.person_id
JOIN movies m1 ON m1.id = s1.movie_id
WHERE s1.movie_id IN (
    SELECT s2.movie_id
    FROM stars s2
    JOIN people p2 ON p2.id = s2.person_id
    JOIN movies m2 ON m2.id = s2.movie_id
    WHERE p2.name = "Kevin Bacon" AND p2.birth = 1958
);
