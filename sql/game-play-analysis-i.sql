/*
Link: https://leetcode.com/problems/game-play-analysis-i/

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
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.
 
Write an SQL query that reports the first login date for each player.
*/
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;