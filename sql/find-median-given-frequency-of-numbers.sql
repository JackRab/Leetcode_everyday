/*
The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.
*/

WITH cum AS (
    SELECT 
        number,
        frequency,
        SUM(frequency) OVER(ORDER BY number) AS cumsum,
        SUM(frequency) OVER()/2 AS median_num  
    FROM Numbers
)

SELECT AVG(number) AS median
FROM cum
WHERE median_num BETWEEN (cumsum-frequency) AND cumsum;