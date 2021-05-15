/*
Link: https://leetcode.com/problems/top-travellers/

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key for this table.
name is the name of the user.
 

Table: Rides
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the primary key for this table.
user_id is the id of the user who travelled the distance "distance".
 

Write an SQL query to report the distance travelled by each user.
*/
SELECT name, CASE WHEN user_id IS NULL THEN 0
             ELSE SUM(distance)
             END AS travelled_distance
FROM Users AS u 
LEFT JOIN Rides AS r 
ON u.id = r.user_id
GROUP BY name
ORDER BY travelled_distance DESC, name; 