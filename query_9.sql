-- Знайти список курсів, які відвідує студент.
SELECT p.student_info, p.lesson
FROM points_table AS p
WHERE p.student_info = 'Alexis Mcdaniel'
GROUP BY p.student_info, p.lesson