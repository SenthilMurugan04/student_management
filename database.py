import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="915097",
            port=3306,
            database="student_management_db"
        )

        return connection

    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None