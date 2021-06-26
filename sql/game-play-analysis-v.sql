/*
Link: https://leetcode.com/problems/game-play-analysis-v/
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
 
We define the install date of a player to be the first login day of that player.

We also define day 1 retention of some date X to be the number of players whose install date is X and they logged back in on the day right after X, divided by the number of players whose install date is X, rounded to 2 decimal places.

Write an SQL query that reports for each install date, the number of players that installed the game on that day and the day 1 retention.

*/

WITH install AS (
    SELECT player_id, MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)

SELECT 
    install_dt, 
    COUNT(DISTINCT i.player_id) AS installs,
    ROUND(COUNT(DISTINCT CASE WHEN DATEDIFF(install_dt, event_date)=-1 THEN i.player_id ELSE NULL END) / COUNT(DISTINCT i.player_id), 2) AS Day1_retention
FROM install AS i
LEFT JOIN activity AS a
ON i.player_id = a.player_id
GROUP BY install_dt;