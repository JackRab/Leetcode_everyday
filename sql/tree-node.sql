/*
Link: https://leetcode.com/problems/tree-node/
Given a table tree, id is identifier of the tree node and p_id is its parent node's id.

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Each node in the tree can be one of three types:
Leaf: if the node is a leaf node.
Root: if the node is the root of the tree.
Inner: If the node is neither a leaf node nor a root node.
 

Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:
*/
SELECT DISTINCT t1.id, CASE WHEN t1.p_id IS NULL THEN 'Root'
                       WHEN (t1.p_id IS NOT NULL) AND t2.id IS NULL THEN 'Leaf'
                       ELSE 'Inner'
                       END AS Type
FROM tree AS t1
LEFT JOIN tree AS t2
ON t1.id = t2.p_id;