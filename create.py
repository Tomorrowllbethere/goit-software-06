import sqlite3
sql_file = 'lessons.sql'
data_base = 'lessons.db'
def create_db():
    # читаємо файл зі скриптом для створення БД
    with open(sql_file, 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(data_base) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
