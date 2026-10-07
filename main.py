from student import student_menu
from course import course_menu
from result import result_menu
from reports import report_menu


# =========================================
# MAIN MENU
# =========================================

def main():

    while True:

        print("\n")
        print("========================================")
        print(" STUDENT COURSE & RESULT MANAGEMENT")
        print("========================================")

        print("1. Student Management")
        print("2. Course Management")
        print("3. Result Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            student_menu()

        elif choice == "2":

            course_menu()

        elif choice == "3":

            result_menu()

        elif choice == "4":

            report_menu()

        elif choice == "5":

            print("\nThank you for using the system.")
            print("Program closed.")
            break

        else:

            print("Invalid choice.")
            print("Please enter a number from 1 to 5.")


# =========================================
# PROGRAM START
# =========================================

if __name__ == "__main__":
    main()