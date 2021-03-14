/*
Link: https://leetcode.com/problems/classes-more-than-5-students/

There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+

Note:
The students should not be counted duplicate in each course.
*/


/* solution 1: use having */
SELECT class 
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;

/* solution 2: use sub-query */
SELECT class 
FROM (SELECT class, COUNT(DISTINCT student) AS num
      FROM course
      GROUP BY class) AS temp
WHERE num >= 5;