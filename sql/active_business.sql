/*
Link: https://leetcode.com/problems/active-businesses/
Table: Events
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurences    | int     | 
+---------------+---------+
(business_id, event_type) is the primary key of this table.
Each row in the table logs the info that an event of some type occured at some business for a number of times.

Write an SQL query to find all active businesses.

An active business is a business that has more than one event type with occurences greater than the average occurences of that event type among all businesses.

*/


SELECT business_id
FROM (
    SELECT business_id, SUM(IF(occurences > avg_occu, 1, 0)) AS num
    FROM (
        SELECT event_type, AVG(occurences) AS avg_occu
        FROM Events
        GROUP BY event_type
    ) AS s
    JOIN Events AS e
    ON e.event_type = s.event_type
    GROUP BY business_id
    ) AS subq
WHERE num > 1;