/*
Link: https://leetcode.com/problems/reported-posts-ii/

Table: Actions
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    |
| action        | enum    |
| extra         | varchar |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
The action column is an ENUM type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
The extra column has optional information about the action such as a reason for report or a type of reaction. 

Table: Removals
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| post_id       | int     |
| remove_date   | date    | 
+---------------+---------+
post_id is the primary key of this table.
Each row in this table indicates that some post was removed as a result of being reported or as a result of an admin review.

Write an SQL query to find the average for daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

*/

SELECT ROUND(AVG(remove_percent), 2) AS average_daily_percent
FROM (
    SELECT action_date, 100*COUNT(DISTINCT r.post_id)/COUNT(DISTINCT a.post_id) AS remove_percent
    FROM Actions AS a 
    LEFT JOIN Removals AS r 
    ON a.post_id = r.post_id
    WHERE extra = 'spam'
    GROUP BY action_date
) AS subq;