/*
Link: https://leetcode.com/problems/apples-oranges/
Table: Sales

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    | 
| sold_num      | int     | 
+---------------+---------+
(sale_date,fruit) is the primary key for this table.
This table contains the sales of "apples" and "oranges" sold each day.
 

Write an SQL query to report the difference between number of apples and oranges sold each day.

Return the result table ordered by sale_date in format ('YYYY-MM-DD').
*/
/* Solution 1: cartesian product */
SELECT s1.sale_date, s1.sold_num - s2.sold_num AS diff
FROM Sales AS s1, Sales AS s2
WHERE s1.sale_date = s2.sale_date AND s1.fruit = 'apples' AND s2.fruit = 'oranges'
ORDER BY s1.sale_date;

/* Solution 2: sum */
SELECT sale_date, SUM(IF(fruit='apples', sold_num, -sold_num)) AS diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date;