# Student Course & Result Management System

## 1. Project Objective

The Student Course & Result Management System is a beginner-friendly console-based Python application connected with MySQL.

The application is used to manage:

* Students
* Courses
* Student results
* Marks
* Grades
* Reports

The project demonstrates Python programming, MySQL connectivity, CRUD operations, SQL queries, JOINs, aggregate functions, input validation, and exception handling.

---

## 2. Technologies Used

* Python
* MySQL
* SQL
* mysql-connector-python

---

## 3. Features

### Student Management

* Add student
* View all students
* View student by ID
* Search student by name
* Update student
* Delete student

### Course Management

* Add course
* View all courses
* Update course
* Delete course
* Search course

### Result Management

* Add result
* View all results
* View result by student
* View result by course
* Automatic grade calculation

### Reports

* Students with course and marks
* Highest mark
* Average marks
* Students above 80
* Number of students in each course
* Failed students

---

## 4. Grade System

| Marks    | Grade |
| -------- | ----- |
| 90 - 100 | A+    |
| 80 - 89  | A     |
| 70 - 79  | B     |
| 60 - 69  | C     |
| 50 - 59  | D     |
| Below 50 | F     |

The grade is calculated automatically by the Python application.

---

## 5. Database Structure

The database name is:

```text
student_management_db
```

The database contains three tables:

```text
students
courses
results
```

### Students Table

```text
student_id
student_name
email
phone
date_of_birth
```

### Courses Table

```text
course_id
course_name
duration
```

### Results Table

```text
result_id
student_id
course_id
marks
grade
```

---

## 6. Table Relationship

The results table contains foreign keys connecting students and courses.

```text
students
    |
    | student_id
    |
    v
results
    ^
    | course_id
    |
courses
```

A student can have multiple results.

A course can have results for multiple students.

---

## 7. Project Structure

```text
student_management_system/
│
├── main.py
├── database.py
├── student.py
├── course.py
├── result.py
├── reports.py
├── schema.sql
├── requirements.txt
└── README.md
```

---

## 8. Installation

### Step 1: Install Python

Make sure Python is installed.

Check:

```bash
python --version
```

---

### Step 2: Install MySQL

Make sure MySQL Server is installed and running.

Check that you can log in to MySQL.

---

### Step 3: Install Python MySQL Connector

Run:

```bash
pip install mysql-connector-python
```

Or:

```bash
pip install -r requirements.txt
```

---

## 9. Database Setup

Open MySQL.

Run the contents of:

```text
schema.sql
```

This creates:

```text
student_management_db
```

and the required tables.

---

## 10. Configure Database Connection

Open:

```text
database.py
```

Update the MySQL username and password.

Example:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management_db"
)
```

If your MySQL password is different, replace `root` with your actual password.

---

## 11. Run the Application

Open terminal inside the project folder.

Run:

```bash
python main.py
```

The application displays:

```text
========================================
 STUDENT COURSE & RESULT MANAGEMENT
========================================
1. Student Management
2. Course Management
3. Result Management
4. Reports
5. Exit

Enter your choice:
```

---

## 12. Application Flow

### Student

```text
Student Management
        |
        +-- Add Student
        +-- View Students
        +-- View Student By ID
        +-- Search Student
        +-- Update Student
        +-- Delete Student
```

### Course

```text
Course Management
        |
        +-- Add Course
        +-- View Courses
        +-- Update Course
        +-- Delete Course
        +-- Search Course
```

### Result

```text
Result Management
        |
        +-- Add Result
        +-- View Results
        +-- View Result By Student
        +-- View Result By Course
```

### Reports

```text
Reports
   |
   +-- All Students With Course And Marks
   +-- Highest Mark
   +-- Average Marks
   +-- Students Above 80
   +-- Students Per Course
   +-- Failed Students
```

---

## 13. SQL Concepts Demonstrated

The project demonstrates:

### CREATE

Used to create the database and tables.

### INSERT

Used to add students, courses and results.

### SELECT

Used to display data.

### UPDATE

Used to update student and course information.

### DELETE

Used to delete students and courses.

### WHERE

Used to filter records.

### LIKE

Used for searching student and course names.

### ORDER BY

Used for sorting records.

### COUNT()

Used to count students.

### AVG()

Used to calculate average marks.

### MAX()

Used to find the highest mark.

### GROUP BY

Used to group students by course.

### INNER JOIN

Used to combine student, course and result information.

---

## 14. Validation

The application validates:

* Empty student name
* Empty course name
* Invalid email
* Invalid student ID
* Invalid course ID
* Invalid marks
* Marks below 0
* Marks above 100
* Duplicate email
* Duplicate course
* Invalid menu choice

---

## 15. Exception Handling

The application uses exception handling to prevent crashes caused by:

* Invalid numeric input
* Database errors
* Duplicate values
* Invalid IDs
* Invalid marks
* Missing students
* Missing courses

---

## 16. Testing

The following test cases should be checked.

### Test 1: Add Student

Enter valid student information.

Expected:

```text
Student added successfully.
```

### Test 2: Empty Student Name

Expected:

```text
Student name cannot be empty.
```

### Test 3: Invalid Email

Expected:

```text
Invalid email format.
```

### Test 4: Invalid Student ID

Enter:

```text
abc
```

Expected:

```text
Student ID must be a number.
```

### Test 5: Invalid Marks

Enter:

```text
120
```

Expected:

```text
Marks must be between 0 and 100.
```

### Test 6: Add Result

Enter valid student, course and marks.

The application automatically calculates the grade.

Example:

```text
Enter marks (0-100): 85

Calculated Grade: A

Result added successfully.
```

### Test 7: Failed Student

Enter:

```text
45
```

Expected:

```text
Grade: F
```

---

## 17. Example Main Menu

```text
========================================
 STUDENT COURSE & RESULT MANAGEMENT
========================================
1. Student Management
2. Course Management
3. Result Management
4. Reports
5. Exit

Enter your choice:
```

---

## 18. Future Improvements

The project can later be extended with:

* Login system
* GUI
* Web application
* REST API
* Admin dashboard
* Export reports to Excel
* Student attendance
* Subject-wise performance
* PDF report generation

---

## 19. Conclusion

This project demonstrates the practical use of Python and MySQL to build a simple Student Course & Result Management System.

It covers Python functions, modules, database connectivity, CRUD operations, SQL queries, JOINs, aggregate functions, validation, and exception handling.
