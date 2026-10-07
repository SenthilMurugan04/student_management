CREATE DATABASE IF NOT EXISTS student_management_db;

USE student_management_db;


-- =========================================
-- STUDENTS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    date_of_birth DATE
);


-- =========================================
-- COURSES TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL UNIQUE,
    duration VARCHAR(50) NOT NULL
);


-- =========================================
-- RESULTS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,

    student_id INT NOT NULL,
    course_id INT NOT NULL,

    marks DECIMAL(5,2) NOT NULL,
    grade VARCHAR(2) NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE,

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
        ON DELETE CASCADE,

    CHECK (marks >= 0 AND marks <= 100)
);