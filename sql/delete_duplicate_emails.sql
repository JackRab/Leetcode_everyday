/*

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql. Use delete statement.

*/

--Solution 1: use delete and inner join
DELETE P1
FROM Person AS P1
INNER JOIN Person AS P2
WHERE P1.Email = P2.email AND P1.Id > P2.Id;

--Solution 2: use count
SELECT Id, Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;

-- Solution 3: Catersian product
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
