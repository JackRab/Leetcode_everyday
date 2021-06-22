/*
Link: https://leetcode.com/problems/get-the-second-most-recent-activity/

Table: UserActivity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| username      | varchar |
| activity      | varchar |
| startDate     | Date    |
| endDate       | Date    |
+---------------+---------+
This table does not contain primary key.
This table contain information about the activity performed of each user in a period of time.
A person with username performed a activity from startDate to endDate.

Write an SQL query to show the second most recent activity of each user.

If the user only has one activity, return that one. 

A user can't perform more than one activity at the same time. Return the result table in any order.
*/

SELECT username, activity, startDate, endDate
FROM (
    SELECT username, activity, startDate, endDate, ROW_NUMBER() OVER(PARTITION BY username ORDER BY startDate DESC) AS row_num, COUNT(activity) OVER(PARTITION BY username) AS count
    FROM UserActivity
) AS subq
WHERE (count = 1 AND row_num = 1) OR (count > 1 AND row_num = 2);
