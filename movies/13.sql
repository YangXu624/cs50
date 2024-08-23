SELECT name, person_id
FROM people
JOIN stars ON people.id = stars.movie_id
WHERE name = "Kevin Bacon";
