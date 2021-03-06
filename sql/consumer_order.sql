/*
Link: https://leetcode.com/problems/customers-who-never-order/

Suppose that a website contains two tables, the Customers table and the Orders table. 
Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

*/

-- Solution 1: use subquery
SELECT Name AS Customers
FROM Customers 
WHERE Id NOT IN (SELECT CustomerId FROM Orders);


-- Solution 2: use anti join from left join
SELECT Name AS Customers
FROM Customers AS C
LEFT JOIN Orders AS O ON O.CustomerId = C.Id
WHERE O.CustomerId IS NULL;