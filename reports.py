from database import get_connection


# =========================================
# REPORT 1
# ALL STUDENTS WITH COURSE AND MARKS
# =========================================

def report_all_students():

    print("\n========== STUDENTS WITH COURSE AND MARKS ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            s.student_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM students s

        INNER JOIN results r
            ON s.student_id = r.student_id

        INNER JOIN courses c
            ON r.course_id = c.course_id

        ORDER BY s.student_name
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No data found.")
            return

        for row in rows:

            print("--------------------------------")
            print("Student ID :", row[0])
            print("Student    :", row[1])
            print("Course     :", row[2])
            print("Marks      :", row[3])
            print("Grade      :", row[4])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# REPORT 2
# HIGHEST MARK
# =========================================

def report_highest_mark():

    print("\n========== HIGHEST MARK ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks
        FROM results r

        INNER JOIN students s
            ON r.student_id = s.student_id

        INNER JOIN courses c
            ON r.course_id = c.course_id

        WHERE r.marks = (
            SELECT MAX(marks)
            FROM results
        )
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No result data found.")
            return

        for row in rows:

            print("--------------------------------")
            print("Student :", row[0])
            print("Course  :", row[1])
            print("Highest Mark :", row[2])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# REPORT 3
# AVERAGE MARKS
# =========================================

def report_average_marks():

    print("\n========== AVERAGE MARKS ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT AVG(marks)
        FROM results
        """

        cursor.execute(query)

        row = cursor.fetchone()

        if row[0] is None:
            print("No result data found.")
        else:
            print("Average Marks:", round(float(row[0]), 2))

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# REPORT 4
# STUDENTS ABOVE 80
# =========================================

def report_above_80():

    print("\n========== STUDENTS ABOVE 80 ==========")

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

        WHERE r.marks > 80

        ORDER BY r.marks DESC
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No students scored above 80.")
            return

        for row in rows:

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
# REPORT 5
# NUMBER OF STUDENTS IN EACH COURSE
# =========================================

def report_students_per_course():

    print("\n========== STUDENTS PER COURSE ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT
            c.course_name,
            COUNT(r.student_id) AS student_count
        FROM courses c

        LEFT JOIN results r
            ON c.course_id = r.course_id

        GROUP BY c.course_id, c.course_name

        ORDER BY student_count DESC
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:

            print("--------------------------------")
            print("Course :", row[0])
            print("Students :", row[1])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# REPORT 6
# FAILED STUDENTS
# =========================================

def report_failed_students():

    print("\n========== FAILED STUDENTS ==========")

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

        WHERE r.marks < 50

        ORDER BY r.marks
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if not rows:
            print("No failed students.")
            return

        for row in rows:

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
# REPORT MENU
# =========================================

def report_menu():

    while True:

        print("\n")
        print("========================================")
        print("              REPORTS")
        print("========================================")

        print("1. All Students With Course And Marks")
        print("2. Highest Mark")
        print("3. Average Marks")
        print("4. Students Above 80")
        print("5. Number Of Students In Each Course")
        print("6. Failed Students")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            report_all_students()

        elif choice == "2":
            report_highest_mark()

        elif choice == "3":
            report_average_marks()

        elif choice == "4":
            report_above_80()

        elif choice == "5":
            report_students_per_course()

        elif choice == "6":
            report_failed_students()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")