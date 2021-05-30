/*
https://leetcode.com/problems/evaluate-boolean-expression/

Table Variables:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
name is the primary key for this table.
This table contains the stored variables and their values.
 

Table Expressions:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
(left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.
 

Write an SQL query to evaluate the boolean expressions in Expressions table.

*/
SELECT left_operand, operator, right_operand, 
       CASE WHEN operator = '>' AND l.value > r.value THEN 'true'
       WHEN operator = '<' AND l.value < r.value THEN 'true'
       WHEN operator = '=' AND l.value = r.value THEN 'true'
       ELSE 'false'
       END AS value
FROM Expressions AS e
JOIN Variables AS l
ON e.left_operand = l.name
JOIN Variables AS r
ON e.right_operand = r.name;