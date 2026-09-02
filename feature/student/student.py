students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    email = input("Enter Email: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "email": email
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_student_details():
    print("\n--- Student Details ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Department :", student["department"])
        print("Email      :", student["email"])


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("-------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Department :", student["department"])
            print("Email      :", student["email"])
            return

    print("\nStudent not found.")