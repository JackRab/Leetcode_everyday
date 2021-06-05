/*
Link: https://leetcode.com/problems/restaurant-growth/
Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) have visited the restaurant.
amount is the total paid by a customer.
 

You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Write an SQL query to compute moving average of how much customer paid in a 7 days window (current day + 6 days before) .
*/
SELECT visited_on, amount, average_amount
FROM (
    SELECT visited_on, amount, ROUND(amount/7, 2) AS average_amount, ROW_NUMBER() OVER() AS number
    FROM (
        SELECT DISTINCT visited_on, SUM(amount) OVER(ORDER BY visited_on RANGE INTERVAL 6 DAY PRECEDING) AS amount
        FROM Customer
    ) AS s1
) AS s2
WHERE number >= 7;