/*
Link: https://leetcode.com/problems/second-highest-salary/
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/

/* A few caveats: 
1) need to return null if no second highest salary
2) there maybe multiple second highest
*/

/* Solution 1: use DENSE_RANK AND CASE */
SELECT CASE WHEN COUNT(Salary) = 0
            THEN NULL
            ELSE Salary
       END AS SecondHighestSalary
FROM (SELECT DISTINCT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) AS my_rank FROM Employee) as r
WHERE my_rank = 2;

/* Solution 2: use Max and sub-query*/
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);


/* Solution 3: use IFNULL */
SELECT IFNULL((SELECT DISTINCT Salary
              FROM Employee
              ORDER BY Salary DESC
              LIMIT 1, 1), NULL) AS SecondHighestSalary;