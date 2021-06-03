/*
Link: https://leetcode.com/problems/last-person-to-fit-in-the-elevator/
Table: Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id is the primary key column for this table.
This table has the information about all people waiting for an elevator.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
 

The maximum weight the elevator can hold is 1000.

Write an SQL query to find the person_name of the last person who will fit in the elevator without exceeding the weight limit. It is guaranteed that the person who is first in the queue can fit in the elevator.
*/
SELECT person_name
FROM (
    SELECT person_name, SUM(weight) OVER(ORDER BY turn) AS total_weight
    FROM Queue
) AS subq
WHERE total_weight <= 1000
ORDER BY 1000 - total_weight
LIMIT 1;