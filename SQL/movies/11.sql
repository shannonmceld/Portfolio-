--In 11.sql, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
--Your query should output a table with a single column for the title of each movie.
--You may assume that there is only one person in the database with the name Chadwick Boseman.

SELECT title FROM movies JOIN ratings ON movies.id = ratings.movie_id AND ratings.rating JOIN stars ON ratings.movie_id = stars.movie_id AND ratings.rating JOIN people ON stars.person_id = people.id WHERE people.name = 'Chadwick Boseman' ORDER BY rating DESC LIMIT 5;