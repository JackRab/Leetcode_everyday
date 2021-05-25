/*
Link: https://leetcode.com/problems/all-people-report-to-the-given-manager/
Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| employee_name | varchar |
| manager_id    | int     |
+---------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates that the employee with ID employee_id and name employee_name reports his work to his/her direct manager with manager_id
The head of the company is the employee with employee_id = 1.
 

Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.
*/
WITH RECURSIVE report(employee_id) AS (
    SELECT employee_id FROM Employees WHERE manager_id = 1 AND employee_id != 1
    UNION ALL
    SELECT e.employee_id 
    FROM report AS r
    JOIN Employees AS e
    ON r.employee_id = e.manager_id
) 
SELECT employee_id
FROM report;