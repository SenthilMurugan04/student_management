from database import get_connection


# =========================================
# ADD COURSE
# =========================================

def add_course():

    print("\n========== ADD COURSE ==========")

    course_name = input("Enter course name: ").strip()

    if course_name == "":
        print("Course name cannot be empty.")
        return

    duration = input("Enter course duration: ").strip()

    if duration == "":
        print("Duration cannot be empty.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        INSERT INTO courses
        (course_name, duration)
        VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (course_name, duration)
        )

        connection.commit()

        print("Course added successfully.")

    except Exception as e:

        connection.rollback()

        if "Duplicate entry" in str(e):
            print("Course already exists.")

        else:
            print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# VIEW COURSES
# =========================================

def view_courses():

    print("\n========== ALL COURSES ==========")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT course_id,
               course_name,
               duration
        FROM courses
        ORDER BY course_id
        """

        cursor.execute(query)

        courses = cursor.fetchall()

        if not courses:
            print("No courses found.")
            return

        for course in courses:

            print("--------------------------------")
            print("Course ID   :", course[0])
            print("Course Name :", course[1])
            print("Duration    :", course[2])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# UPDATE COURSE
# =========================================

def update_course():

    print("\n========== UPDATE COURSE ==========")

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

        cursor.execute(
            "SELECT * FROM courses WHERE course_id = %s",
            (course_id,)
        )

        course = cursor.fetchone()

        if course is None:
            print("Course not found.")
            return

        name = input("Enter new course name: ").strip()
        duration = input("Enter new duration: ").strip()

        if name == "":
            name = course[1]

        if duration == "":
            duration = course[2]

        query = """
        UPDATE courses
        SET course_name = %s,
            duration = %s
        WHERE course_id = %s
        """

        cursor.execute(
            query,
            (name, duration, course_id)
        )

        connection.commit()

        print("Course updated successfully.")

    except Exception as e:

        connection.rollback()

        if "Duplicate entry" in str(e):
            print("Course already exists.")

        else:
            print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# DELETE COURSE
# =========================================

def delete_course():

    print("\n========== DELETE COURSE ==========")

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

        cursor.execute(
            "SELECT course_name FROM courses WHERE course_id = %s",
            (course_id,)
        )

        course = cursor.fetchone()

        if course is None:
            print("Course not found.")
            return

        print("Course:", course[0])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() != "yes":
            print("Delete cancelled.")
            return

        cursor.execute(
            "DELETE FROM courses WHERE course_id = %s",
            (course_id,)
        )

        connection.commit()

        print("Course deleted successfully.")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# SEARCH COURSE
# =========================================

def search_course():

    print("\n========== SEARCH COURSE ==========")

    name = input("Enter course name: ").strip()

    if name == "":
        print("Course name cannot be empty.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        query = """
        SELECT course_id,
               course_name,
               duration
        FROM courses
        WHERE course_name LIKE %s
        ORDER BY course_name
        """

        cursor.execute(query, ("%" + name + "%",))

        courses = cursor.fetchall()

        if not courses:
            print("No course found.")
            return

        for course in courses:

            print("--------------------------------")
            print("Course ID   :", course[0])
            print("Course Name :", course[1])
            print("Duration    :", course[2])

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# =========================================
# COURSE MENU
# =========================================

def course_menu():

    while True:

        print("\n")
        print("========================================")
        print("          COURSE MANAGEMENT")
        print("========================================")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Search Course")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_course()

        elif choice == "2":
            view_courses()

        elif choice == "3":
            update_course()

        elif choice == "4":
            delete_course()

        elif choice == "5":
            search_course()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")