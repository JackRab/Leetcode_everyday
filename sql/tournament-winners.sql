/*
Link: https://leetcode.com/problems/tournament-winners/

Table: Players
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| player_id   | int   |
| group_id    | int   |
+-------------+-------+
player_id is the primary key of this table.
Each row of this table indicates the group of each player.

Table: Matches
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| first_player  | int     |
| second_player | int     | 
| first_score   | int     |
| second_score  | int     |
+---------------+---------+
match_id is the primary key of this table.
Each row is a record of a match, first_player and second_player contain the player_id of each match.
first_score and second_score contain the number of points of the first_player and second_player respectively.
You may assume that, in each match, players belongs to the same group.

The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

Write an SQL query to find the winner in each group.

*/

WITH m AS (
    SELECT first_player AS player_id, first_score AS score
    FROM Matches
    UNION ALL
    SELECT second_player AS player_id, second_score AS score
    FROM Matches
),
s AS (
    SELECT p.group_id, m.player_id, SUM(score) AS score
    FROM m 
    JOIN Players AS p 
    ON m.player_id = p.player_id
    GROUP BY p.group_id, m.player_id
)
SELECT group_id, player_id
FROM (
    SELECT group_id, player_id, ROW_NUMBER() OVER(PARTITION BY group_id ORDER BY score DESC, player_id ASC) AS num 
    FROM s
    ORDER BY num, player_id
) AS subq
WHERE num = 1
ORDER BY group_id;