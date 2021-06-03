/*
Link: https://leetcode.com/problems/the-most-recent-three-orders/

Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the primary key for this table.
This table contains information about customers.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| cost          | int     |
+---------------+---------+
order_id is the primary key for this table.
This table contains information about the orders made by customer_id.
Each customer has one order per day.
 

Write an SQL query to find the most recent 3 orders of each user. If a user ordered less than 3 orders return all of their orders.
*/
SELECT name AS customer_name, customer_id, order_id, order_date
FROM (
    SELECT name, o.customer_id, order_id, order_date, RANK() OVER(PARTITION BY c.customer_id ORDER BY order_date DESC) AS `rank`
    FROM Customers AS c
    JOIN Orders AS o
    ON c.customer_id = o.customer_id
) AS subq
WHERE `rank` <= 3
ORDER BY customer_name, customer_id, order_date DESC;