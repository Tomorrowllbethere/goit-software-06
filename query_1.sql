SELECT AVG(p.points), st.full_name
FROM points_table as p
LEFT JOIN students as st ON  st.full_name = p.student_info
GROUP BY st.full_name
LIMIT 5;