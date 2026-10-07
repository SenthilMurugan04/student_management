from database import get_connection


# =========================================
# CALCULATE GRADE
# =========================================

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


# =========================================
# ADD RESULT
# =========================================

def add_result():

    print("\n========== ADD RESULT ==========")

    try:

        student_id = int(input("Enter student ID: "))

    except ValueError:

        print("Student ID must be a number.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        # Check student

        cursor.execute(
            "SELECT student_name FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        print("Student:", student[0])

        # Course ID

        try:

            course_id = int(input("Enter course ID: "))

        except ValueError:

            print("Course ID must be a number.")
            return

        # Check course

        cursor.execute(
            "SELECT course_name FROM courses WHERE course_id = %s",
            (course_id,)
        )

        course = cursor.fetchone()

        if course is None:
            print("Course not found.")
            return

        print("Course:", course[0])

        # Marks

        try:

            marks = float(input("Enter marks (0-100): "))

        except ValueError:

            print("Marks must be a number.")
            return

        if marks < 0 or marks > 100:

            print("Marks must be between 0 and 100.")
            return

        # Grade

        grade = calculate_grade(marks)

        print("Calculated Grade:", grade)

        # Insert

        query = """
        INSERT INTO results
        (student_id, course_id, marks, grade)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (student_id, course_id, marks, grade)
        )

        connection.commit()

        print("Result added successfully.")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW ALL RESULTS
# =========================================

def view_results():

    print("\n========== ALL RESULTS ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            r.result_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r
        INNER JOIN students s
            ON r.student_id = s.student_id
        INNER JOIN courses c
            ON r.course_id = c.course_id
        ORDER BY r.result_id
        """

        cursor.execute(query)

        results = cursor.fetchall()

        if not results:
            print("No results found.")
            return

        for row in results:

            print("--------------------------------")
            print("Result ID   :", row[0])
            print("Student     :", row[1])
            print("Course      :", row[2])
            print("Marks       :", row[3])
            print("Grade       :", row[4])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW RESULT BY STUDENT
# =========================================

def view_result_by_student():

    print("\n========== STUDENT RESULT ==========")

    try:

        student_id = int(input("Enter student ID: "))

    except ValueError:

        print("Student ID must be a number.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r

        INNER JOIN students s
            ON r.student_id = s.student_id

        INNER JOIN courses c
            ON r.course_id = c.course_id

        WHERE s.student_id = %s
        """

        cursor.execute(query, (student_id,))

        results = cursor.fetchall()

        if not results:
            print("No result found for this student.")
            return

        for row in results:

            print("--------------------------------")
            print("Student :", row[0])
            print("Course  :", row[1])
            print("Marks   :", row[2])
            print("Grade   :", row[3])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW RESULT BY COURSE
# =========================================

def view_result_by_course():

    print("\n========== COURSE RESULTS ==========")

    try:

        course_id = int(input("Enter course ID: "))

    except ValueError:

        print("Course ID must be a number.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            c.course_name,
            s.student_name,
            r.marks,
            r.grade
        FROM results r

        INNER JOIN students s
            ON r.student_id = s.student_id

        INNER JOIN courses c
            ON r.course_id = c.course_id

        WHERE c.course_id = %s
        ORDER BY r.marks DESC
        """

        cursor.execute(query, (course_id,))

        results = cursor.fetchall()

        if not results:
            print("No result found for this course.")
            return

        for row in results:

            print("--------------------------------")
            print("Course  :", row[0])
            print("Student :", row[1])
            print("Marks   :", row[2])
            print("Grade   :", row[3])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# RESULT MENU
# =========================================

def result_menu():

    while True:

        print("\n")
        print("========================================")
        print("           RESULT MANAGEMENT")
        print("========================================")
        print("1. Add Result")
        print("2. View All Results")
        print("3. View Result By Student")
        print("4. View Result By Course")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_result()

        elif choice == "2":
            view_results()

        elif choice == "3":
            view_result_by_student()

        elif choice == "4":
            view_result_by_course()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")