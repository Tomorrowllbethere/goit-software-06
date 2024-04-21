-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name VARCHAR(255) UNIQUE NOT NULL
);

--Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    group_name TEXT,
    student_in VARCHAR(255) NOT NULL,
    FOREIGN KEY (student_in) REFERENCES students (full_name),
    FOREIGN KEY (group_name) REFERENCES subjects (lesson_group)
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    teacher_full_name VARCHAR(255) UNIQUE NOT NULL
);
-- Table: lessons/teachers
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    lesson_name TEXT,
    lesson_teacher VARCHAR(255),
    lesson_group TEXT,
    FOREIGN KEY (lesson_name) REFERENCES points_table(lesson),
    FOREIGN KEY (lesson_teacher) REFERENCES teachers(teacher_full_name),
    FOREIGN KEY (lesson_group) REFERENCES groups(group_name)
      
);
-- Table with points
DROP TABLE IF EXISTS points_table;
CREATE TABLE points_table (
    student_info VARCHAR(255) NOT NULL,
    lesson TEXT,
    points FLOAT,
    date_of DATETIME,
    FOREIGN KEY (student_info) REFERENCES students (full_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);