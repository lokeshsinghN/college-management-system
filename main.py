from feature.student.student import (
    add_student,
    display_student_details,
    search_student
)


def main():

    while True:

        print("\n===== COLLEGE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Student Details")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_student_details()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()