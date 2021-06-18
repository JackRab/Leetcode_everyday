/*
Link: https://leetcode.com/problems/count-student-number-in-departments/
A university uses 2 data tables, student and department, to store data about its students and the departments associated with each major.

Write a query to print the respective department name and number of students majoring in each department for all departments in the department table (even ones with no current students).

Sort your results by descending number of students; if two or more departments have the same number of students, then sort those departments alphabetically by department name.

The student is described as follow:

| Column Name  | Type      |
|--------------|-----------|
| student_id   | Integer   |
| student_name | String    |
| gender       | Character |
| dept_id      | Integer   |
where student_id is the student's ID number, student_name is the student's name, gender is their gender, and dept_id is the department ID associated with their declared major.

And the department table is described as below:

| Column Name | Type    |
|-------------|---------|
| dept_id     | Integer |
| dept_name   | String  |
where dept_id is the department's ID number and dept_name is the department name.

*/

SELECT dept_name, COUNT(student_id) AS student_number
FROM department AS d
LEFT JOIN student AS s
ON d.dept_id = s.dept_id
GROUP BY dept_name
ORDER BY student_number DESC, dept_name;