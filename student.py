import re
from database import get_connection


# =========================================
# VALIDATE EMAIL
# =========================================

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# =========================================
# ADD STUDENT
# =========================================

def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    email = input("Enter email: ").strip()

    if not validate_email(email):
        print("Invalid email format.")
        return

    phone = input("Enter phone number: ").strip()

    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        INSERT INTO students
        (student_name, email, phone, date_of_birth)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, email, phone, dob)

        cursor.execute(query, values)

        connection.commit()

        print("Student added successfully.")

    except Exception as e:

        connection.rollback()

        if "Duplicate entry" in str(e):
            print("Email already exists.")

        else:
            print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW ALL STUDENTS
# =========================================

def view_students():

    print("\n========== ALL STUDENTS ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT student_id,
               student_name,
               email,
               phone,
               date_of_birth
        FROM students
        ORDER BY student_id
        """

        cursor.execute(query)

        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        for student in students:

            print("--------------------------------")
            print("Student ID :", student[0])
            print("Name       :", student[1])
            print("Email      :", student[2])
            print("Phone      :", student[3])
            print("DOB        :", student[4])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW STUDENT BY ID
# =========================================

def view_student_by_id():

    print("\n========== FIND STUDENT ==========")

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
        SELECT student_id,
               student_name,
               email,
               phone,
               date_of_birth
        FROM students
        WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        print("--------------------------------")
        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Email      :", student[2])
        print("Phone      :", student[3])
        print("DOB        :", student[4])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# SEARCH STUDENT BY NAME
# =========================================

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT student_id,
               student_name,
               email,
               phone,
               date_of_birth
        FROM students
        WHERE student_name LIKE %s
        ORDER BY student_name
        """

        cursor.execute(query, ("%" + name + "%",))

        students = cursor.fetchall()

        if not students:
            print("No matching student found.")
            return

        for student in students:

            print("--------------------------------")
            print("Student ID :", student[0])
            print("Name       :", student[1])
            print("Email      :", student[2])
            print("Phone      :", student[3])
            print("DOB        :", student[4])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# UPDATE STUDENT
# =========================================

def update_student():

    print("\n========== UPDATE STUDENT ==========")

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

        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        print("\nLeave field empty to keep existing value.")

        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        phone = input("Enter new phone: ").strip()

        if name == "":
            name = student[1]

        if email == "":
            email = student[2]

        elif not validate_email(email):
            print("Invalid email format.")
            return

        if phone == "":
            phone = student[3]

        query = """
        UPDATE students
        SET student_name = %s,
            email = %s,
            phone = %s
        WHERE student_id = %s
        """

        values = (name, email, phone, student_id)

        cursor.execute(query, values)

        connection.commit()

        print("Student updated successfully.")

    except Exception as e:

        connection.rollback()

        if "Duplicate entry" in str(e):
            print("Email already exists.")

        else:
            print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# DELETE STUDENT
# =========================================

def delete_student():

    print("\n========== DELETE STUDENT ==========")

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

        cursor.execute(
            "SELECT student_name FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        print("Student:", student[0])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() != "yes":
            print("Delete cancelled.")
            return

        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )

        connection.commit()

        print("Student deleted successfully.")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# STUDENT MENU
# =========================================

def student_menu():

    while True:

        print("\n")
        print("========================================")
        print("         STUDENT MANAGEMENT")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student By ID")
        print("4. Search Student")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            view_student_by_id()

        elif choice == "4":
            search_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")