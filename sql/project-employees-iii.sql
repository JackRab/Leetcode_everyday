/*
Link: https://leetcode.com/problems/project-employees-iii/
Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table.
 

Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.
*/

WITH Most_experienced AS (
    SELECT project_id, MAX(experience_years) AS max_exp_years
    FROM Project AS p 
    JOIN Employee AS e 
    ON p.employee_id = e.employee_id
    GROUP BY project_id
)
SELECT p.project_id, p.employee_id
FROM Project AS p 
JOIN Employee AS e 
ON p.employee_id = e.employee_id
JOIN Most_experienced AS m 
ON p.project_id = m.project_id AND e.experience_years = m.max_exp_years;