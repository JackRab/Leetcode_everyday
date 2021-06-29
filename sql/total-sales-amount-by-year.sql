/*
Link: https://leetcode.com/problems/total-sales-amount-by-year/

Table: Product
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
+---------------+---------+
product_id is the primary key for this table.
product_name is the name of the product.
 
Table: Sales
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| product_id          | int     |
| period_start        | date    |
| period_end          | date    |
| average_daily_sales | int     |
+---------------------+---------+
product_id is the primary key for this table. 
period_start and period_end indicates the start and end date for sales period, both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.

Write an SQL query to report the Total sales amount of each item for each year, with corresponding product name, product_id, product_name and report_year.
*/

WITH RECURSIVE d AS (
    SELECT MIN(period_start) AS date FROM sales
    UNION ALL 
    SELECT date + INTERVAL 1 DAY 
    FROM d 
    WHERE date < (SELECT MAX(period_end) FROM sales)
),
s AS (
    SELECT date, product_id, period_start, period_end, average_daily_sales
    FROM sales
    LEFT JOIN d 
    ON date BETWEEN period_start AND period_end
)

SELECT s.product_id, product_name, LEFT(date, 4) AS report_year, SUM(average_daily_sales) AS total_amount
FROM s 
JOIN Product AS p 
ON s.product_id = p.product_id
GROUP BY s.product_id, product_name, report_year
ORDER BY s.product_id, report_year;