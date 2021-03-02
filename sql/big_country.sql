-- Link: https://leetcode.com/problems/big-countries/

-- A country is big if it has an area of bigger than 3 million square km or 
-- a population of more than 25 million.

-- Write a SQL solution to output big countries' name, population and area.

-- solution 1: use WHERE
SELECT name, population, area
FROM world
WHERE area > 3000000 OR population > 25000000;

-- solution 2: use HAVING
SELECT name, population, area
FROM world
HAVING area > 3000000 OR population > 25000000;

-- solution 3: use UNION
SELECT name, population, area
FROM world
WHERE area > 3000000
UNION
SELECT name, population, area
FROM world
WHERE population > 25000000;