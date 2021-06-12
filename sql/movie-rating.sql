/*
Link: https://leetcode.com/problems/movie-rating/
Table: Movies
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key for this table.
title is the name of the movie.

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key for this table.

Table: Movie_Rating
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 

Write the following SQL query:
Find the name of the user who has rated the greatest number of movies.
In case of a tie, return lexicographically smaller user name.

Find the movie name with the highest average rating in February 2020.
In case of a tie, return lexicographically smaller movie name.
*/
(
    SELECT u.name
    FROM Movie_Rating AS m 
    JOIN Users AS u 
    ON m.user_id = u.user_id
    GROUP BY u.name
    ORDER BY COUNT(movie_id) DESC, u.name
    LIMIT 1
)
UNION
(
    SELECT m.title
    FROM Movie_Rating AS r
    JOIN Movies AS m 
    ON r.movie_id = m.movie_id
    WHERE SUBSTR(created_at, 1, 7) = '2020-02'
    GROUP BY m.title
    ORDER BY AVG(rating) DESC, m.title
    LIMIT 1
)