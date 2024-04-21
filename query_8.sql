-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT s.lesson_teacher, s.lesson_name, AVG(p.points)
FROM subjects AS s
FULL JOIN points_table AS p ON p.lesson = s.lesson_name
GROUP BY s.lesson_teacher, s.lesson_name;
