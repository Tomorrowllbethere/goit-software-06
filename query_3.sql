SELECT p.lesson, AVG(p.points),  g.group_name
FROM points_table AS p
FULL JOIN groups AS g ON g.student_in = p.student_info
GROUP BY g.group_name
