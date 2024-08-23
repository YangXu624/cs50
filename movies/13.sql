SELECT title, name, person_id
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE name = "Kevin Bacon" and birth = 1958;
