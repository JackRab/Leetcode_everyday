/*
Link: https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/

Table: Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the ID in a log Table.

Since some IDs have been removed from Logs. Write an SQL query to find the start and end number of continuous ranges in table Logs.

Order the result table by start_id.
*/
/* Solution 1 */
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM (
    SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) AS num 
    FROM Logs
) AS subq
GROUP BY log_id - num;

/* Solution 2 */
SELECT l1.log_id AS start_id, l2.log_id AS end_id
FROM
    (SELECT log_id
    FROM Logs
    WHERE log_id - 1 NOT IN (SELECT log_id FROM Logs) ) AS l1,
    (SELECT log_id
    FROM Logs
    WHERE log_id + 1 NOT IN (SELECT log_id FROM Logs) ) AS l2
WHERE l1.log_id <= l2.log_id
GROUP BY start_id;