/*
Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the id and the name of an employee in a company.
 

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
 

Write an SQL query to show the unique ID of each user, If a user doesn't have a unique ID replace just show null.
*/

SELECT unique_id, name
FROM Employees AS e1
LEFT JOIN EmployeeUNI AS e2
ON e1.id = e2.id;
