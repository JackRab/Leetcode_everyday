/*
Link: https://leetcode.com/problems/exchange-seats/
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

Note:

If the number of students is odd, there is no need to change the last one's seat.
*/

/* solution 1: use CASE */
SELECT (CASE WHEN MOD(id, 2) != 0 AND max_id != id THEN id+1
             WHEN MOD(id, 2) != 0 AND max_id = id THEN id
             ELSE id-1
       END) AS id, student
FROM seat, (SELECT MAX(id) AS max_id FROM seat) AS mid
ORDER BY id ASC;