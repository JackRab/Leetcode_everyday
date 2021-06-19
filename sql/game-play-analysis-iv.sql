/*
Link: https://leetcode.com/problems/game-play-analysis-iv/

Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some game.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write an SQL query that reports the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

*/

WITH min_date AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),

agg AS (
    SELECT player_id, event_date, SUM(games_played) AS total 
    FROM Activity
    GROUP BY player_id, event_date
)

SELECT ROUND(SUM(IF(event_date - first_login=1, 1, 0))/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM min_date AS m 
JOIN agg AS a 
ON m.player_id = a.player_id;