/*
Link: https://leetcode.com/problems/report-contiguous-dates/

Table: Failed
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| fail_date    | date    |
+--------------+---------+
Primary key for this table is fail_date.
Failed table contains the days of failed tasks.

Table: Succeeded
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| success_date | date    |
+--------------+---------+
Primary key for this table is success_date.
Succeeded table contains the days of succeeded tasks.

A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.
*/

WITH s AS (
    SELECT fail_date AS date, 'failed' AS period_state FROM Failed
    UNION ALL
    SELECT success_date AS date, 'succeeded' AS period_state FROM Succeeded
),
r AS (
    SELECT date, period_state, ROW_NUMBER() OVER(ORDER BY period_state, date) AS num 
    FROM s 
    WHERE date >= '2019-01-01' AND date <= '2019-12-31'
)

SELECT period_state, min(date) AS start_date, max(date) AS end_date
FROM r
GROUP BY DATE_SUB(date, INTERVAL num DAY), period_state
ORDER BY start_date;