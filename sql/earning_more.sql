/*
Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. 
For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

*/

-- Solution 1: use JOIN
SELECT e1.Name as Employee
FROM Employee AS e1
INNER JOIN Employee AS e2
ON e1.ManagerId = e2.Id
WHERE e1.Salary > e2.Salary;


-- Solution 2: use subquery, much slower
SELECT Name as Employee
FROM Employee AS e1
WHERE Salary > (SELECT Salary FROM Employee AS e2 WHERE e2.Id = e1.ManagerId);


-- Solution 3: use cartisian product of two tables 
SELECT Name
FROM Employee AS e1, Employee AS e2
WHERE e1.ManagerId = e2.Id and e1.Salary > e2.Salary;
