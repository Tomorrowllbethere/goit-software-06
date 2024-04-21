import datetime 
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GROUPS = 3
NUMBER_POINTS = 20
cours_file = 'lessons.txt'
groups_file = 'students_group.txt'
database = 'lessons.db'

def generate_fake_data(number_students, number_teфchers, number_subjects,  cours_file) -> tuple():
    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо викладачів
    fake_subjects = []  # тут зберігатимемо уроки
    fake_points = []
    fake_groups = []
    fake_datetime_stamp = []
 
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()
    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_teфchers):
        fake_teachers.append(fake_data.name())
    # Та number_post набір дисциплін
    with open(cours_file, 'r+') as fh:
        lines = fh.readlines()
        lines = [line.strip() for line in lines]
        for _ in range(number_subjects):
            random_lines = choice(lines)
            fake_subjects.append(random_lines)
    # for points of students
    for _ in range(50):
        fake_points.append(float(randint(45, 100)))

   
    with open(groups_file, 'r+') as f:
        groups = f.readlines()
        for _ in range(NUMBER_GROUPS+1):
            group_found = choice([group.strip() for group in groups])
            fake_groups.append(group_found)

    for i in range(60):
        period =  datetime.datetime.today()- datetime.timedelta(days=i, minutes=float(randint(1,59)), hours=float(randint(1,12)))
        date = datetime.datetime.strftime(period, '%H:%M %d-%m-%Y')
        fake_datetime_stamp.append(date)

    return fake_students, fake_teachers, fake_subjects, fake_groups, fake_points, fake_datetime_stamp


# companies, employees, posts = generate_fake_data(NUMBER_STUDENTS, NUMBER_LESSONS, NUMBER_TEACHERS, cours_file)
# print(companies)
# print(employees)
# print(posts)

def prepare_data(students=list, teachers=list, subjects=list, fake_groups=list, fake_points=list, fake_datetime_stamp=list) -> tuple():
    # Готуємо список кортежів 
    new_numb = [i for i in range(1, NUMBER_STUDENTS+1)]
    new_list = [student for student in students]
    for_students = list(zip(new_list, new_numb))

    # для таблиці teachers
    numb_teach = [i for i in range(1, NUMBER_TEACHERS +1)]
    list_teach = [teacher for teacher in teachers]
    for_teachers = list(zip( list_teach, numb_teach))
    
    for_subjects = []
    for i in range(NUMBER_GROUPS):
        for teacher in teachers:
            for_subjects.append((teacher, choice(fake_groups),choice(subjects), ))
               
    for_points = []
    for student in students:
            for i in range(NUMBER_POINTS):
                for_points.append((student, choice(fake_points), choice(subjects), choice(fake_datetime_stamp), ))
    for_groups = []
    for student in students:
        for_groups.append((choice(fake_groups), student, ))
        

    return for_students, for_teachers, for_subjects,  for_groups, for_points


def insert_data_to_db(students, teachers, subjects, groups, points) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        sql_to_students = """INSERT INTO students(full_name, id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)
        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні
        sql_to_teachers = """INSERT INTO teachers (teacher_full_name, id)
                               VALUES (?, ?)"""
        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію
        cur.executemany(sql_to_teachers, teachers)
        # Останньою заповнюємо таблицю
        sql_to_subjects = """INSERT INTO subjects ( lesson_teacher, lesson_group, lesson_name)
                              VALUES (?, ?, ?)"""
        # sql_to_subjects = """INSERT INTO subjects (lesson_teacher)
        #                       VALUES (?)"""
        cur.executemany(sql_to_subjects, subjects)
        sql_to_groups = """INSERT INTO groups (group_name, student_in)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_groups, groups)
        sql_to_points = """INSERT INTO points_table (student_info, points, lesson, date_of)
                              VALUES (?, ?, ?, ?)"""
        # sql_to_points = """INSERT INTO points_table (points)
        #                       VALUES (?)"""

        cur.executemany(sql_to_points, points)
        # Фіксуємо наші зміни в БД
        con.commit()

if __name__ == "__main__":
    students, teachers, subjects, groups, points, datestamp = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS, cours_file)
    students, teachers, subjects, groups, points  = prepare_data(students, teachers, subjects, groups, points, datestamp)
    # print(students) #/done
    # print(teachers) 
    # for sub in subjects:
    #         print(sub)
    # print(subjects) 
    # print(groups)
    # print(points)
    # for point in points:
    #     print(point)
    insert_data_to_db(students, teachers, subjects, groups, points)