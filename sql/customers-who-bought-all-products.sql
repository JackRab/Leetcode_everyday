/*
Link: https://leetcode.com/problems/customers-who-bought-all-products/

Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
product_key is a foreign key to Product table.
 

Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key column for this table.
 
Write an SQL query for a report that provides the customer ids from the Customer table that bought all the products in the Product table.
*/
SELECT customer_id
FROM (
    SELECT customer_id, COUNT(DISTINCT c.product_key) AS count
    FROM Customer AS c
    JOIN Product AS p 
    ON c.product_key = p.product_key
    GROUP BY customer_id
) AS subq
WHERE count = (SELECT COUNT(DISTINCT product_key) FROM Product);
