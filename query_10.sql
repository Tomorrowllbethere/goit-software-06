-- Список курсів, які певному студенту читає певний викладач.
SELECT sub.lesson_teacher, sub.lesson_name, p.student_info
FROM subjects AS sub
LEFT JOIN groups AS g ON g.group_name = sub.lesson_group
LEFT JOIN points_table AS p ON p.lesson = sub.lesson_name AND p.student_info = g.student_in
WHERE g.student_in = 'Connie Johnson' AND sub.lesson_teacher = 'Amanda Fernandez'
GROUP BY g.student_in, sub.lesson_teacher