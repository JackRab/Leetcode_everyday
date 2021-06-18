/*
Link: https://leetcode.com/problems/monthly-transactions-ii/
Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
Table: Chargebacks

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| trans_id       | int     |
| trans_date     | date    |
+----------------+---------+
Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
trans_id is a foreign key to the id column of Transactions table.
Each chargeback corresponds to a transaction made previously even if they were not approved.
 

Write an SQL query to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

Note: In your query, given the month and country, ignore rows with all zeros.

*/
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, 
       SUM(IF(state='approved', 1, 0)) AS approved_count, 
       SUM(IF(state='approved', amount, 0)) AS approved_amount, 
       SUM(IF(state='chargebacked', 1, 0)) AS chargeback_count, 
       SUM(IF(state='chargebacked', amount, 0)) AS chargeback_amount
FROM
(
    (SELECT trans_id AS id, country, 'chargebacked' AS state, amount, c.trans_date
    FROM Chargebacks AS c
    LEFT JOIN Transactions AS t
    ON c.trans_id = t.id
    )
    UNION ALL
    (SELECT * FROM Transactions
     WHERE state = 'approved'
    )
) AS subq
GROUP BY month, country;