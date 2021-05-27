/*
Link: https://leetcode.com/problems/calculate-salaries/
Table Salaries:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| company_id    | int     |
| employee_id   | int     |
| employee_name | varchar |
| salary        | int     |
+---------------+---------+
(company_id, employee_id) is the primary key for this table.
This table contains the company id, the id, the name and the salary for an employee.
 

Write an SQL query to find the salaries of the employees after applying taxes.

The tax rate is calculated for each company based on the following criteria:

0% If the max salary of any employee in the company is less than 1000$.
24% If the max salary of any employee in the company is in the range [1000, 10000] inclusive.
49% If the max salary of any employee in the company is greater than 10000$.
Return the result table in any order. Round the salary to the nearest integer.
*/
WITH Max_salaries AS (
    SELECT company_id, MAX(salary) AS max_salary
    FROM Salaries
    GROUP BY company_id
)
SELECT s.company_id, employee_id, employee_name, ROUND(CASE WHEN max_salary < 1000 THEN salary
                                                 WHEN max_salary > 10000 THEN salary*0.51
                                                 ELSE salary*0.76
                                                 END) AS salary
FROM Salaries AS s
JOIN Max_salaries AS m
ON s.company_id = m.company_id;
