/*
https://leetcode.com/problems/product-price-at-a-given-date/
Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
*/
SELECT o.product_id, IF(o.max_date IS NULL, 10, po.new_price) AS price
FROM (
    SELECT DISTINCT p.product_id, i.max_date
    FROM Products AS p
    LEFT JOIN (
        SELECT product_id, MAX(change_date) AS max_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
        ) AS i
    ON p.product_id = i.product_id
    ) AS o
LEFT JOIN Products AS po
ON po.product_id = o.product_id AND o.max_date = po.change_date;