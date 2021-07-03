/*
Link:https://leetcode.com/problems/number-of-transactions-per-visit/

Table: Visits

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| visit_date    | date    |
+---------------+---------+
(user_id, visit_date) is the primary key for this table.
Each row of this table indicates that user_id has visited the bank in visit_date.
 

Table: Transactions

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| user_id          | int     |
| transaction_date | date    |
| amount           | int     |
+------------------+---------+
There is no primary key for this table, it may contain duplicates.
Each row of this table indicates that user_id has done a transaction of amount in transaction_date.
It is guaranteed that the user has visited the bank in the transaction_date.(i.e The Visits table contains (user_id, transaction_date) in one row)
 

A bank wants to draw a chart of the number of transactions bank visitors did in one visit to the bank and the corresponding number of visitors who have done this number of transaction in one visit.

Write an SQL query to find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction and so on.
*/
WITH cte AS (
    SELECT num AS transactions_count, COUNT(user_id) AS visits_count
    FROM (
        SELECT v.user_id, visit_date, SUM(IF(transaction_date IS NULL, 0, 1)) AS num
        FROM Visits AS v 
        LEFT JOIN Transactions AS t 
        ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
        GROUP BY v.user_id, visit_date
    ) AS subq
    GROUP BY num
),
seq AS (
    SELECT 0 AS num 
    UNION ALL
    SELECT ROW_NUMBER() OVER() AS num FROM cte
)
SELECT s.num AS transactions_count, IFNULL(visits_count, 0) AS visits_count
FROM seq AS s 
LEFT JOIN cte AS c
ON s.num = c.transactions_count;