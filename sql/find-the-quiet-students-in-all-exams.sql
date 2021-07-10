/*
Link: https://leetcode.com/problems/find-the-quiet-students-in-all-exams/

Table: Student
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| student_id          | int     |
| student_name        | varchar |
+---------------------+---------+
student_id is the primary key for this table.
student_name is the name of the student.
 
Table: Exam
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| exam_id       | int     |
| student_id    | int     |
| score         | int     |
+---------------+---------+
(exam_id, student_id) is the primary key for this table.
Student with student_id got score points in exam with id exam_id.

A "quite" student is the one who took at least one exam and didn't score neither the high score nor the low score.

Write an SQL query to report the students (student_id, student_name) being "quiet" in ALL exams.

*/

WITH min_max AS (
    SELECT exam_id, MIN(score) AS min_score, MAX(score) AS max_score
    FROM Exam
    GROUP BY exam_id
),
quiet_t AS (
    SELECT e.exam_id, e.student_id, student_name, score, CASE WHEN score > min_score AND score < max_score THEN 1 ELSE 0 END AS quiet
    FROM Exam AS e 
    JOIN min_max AS m 
    ON e.exam_id = m.exam_id
    JOIN Student AS s 
    ON e.student_id = s.student_id
)

SELECT student_id, student_name
FROM quiet_t 
GROUP BY student_id, student_name
HAVING AVG(quiet) = 1
ORDER BY student_id;