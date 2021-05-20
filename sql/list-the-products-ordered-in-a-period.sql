/*
Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/

Table: Products
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key for this table.
This table contains data about the company's products.

Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
There is no primary key for this table. It may have duplicate rows.
product_id is a foreign key to Products table.
unit is the number of products ordered in order_date.
 
Write an SQL query to get the names of products with greater than or equal to 100 units ordered in February 2020 and their amount.
*/
SELECT product_name, SUM(unit) AS unit
FROM Products AS p 
JOIN Orders AS o 
ON p.product_id = o.product_id
WHERE LEFT(order_date, 7) = '2020-02'
GROUP BY product_name
HAVING unit >= 100;