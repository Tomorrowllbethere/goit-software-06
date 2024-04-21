import sqlite3
sql_file = 'lessons.sql'
data_base = 'lessons.db'

def execute_query(sql: str) -> list:
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT AVG(p.points), st.full_name
FROM points_table as p
LEFT JOIN students as st ON  st.full_name = p.student_info
GROUP BY st.full_name
LIMIT 5;
"""


print(execute_query(sql))