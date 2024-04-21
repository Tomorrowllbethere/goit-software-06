SELECT p_t.points
FROM points_table AS p_t 
FULL JOIN groups AS g ON g.student_in = p_t.student_info
WHERE g.group_name = 'Lin-2' AND p_t.lesson = 'Geology'
ORDER BY g.group_name