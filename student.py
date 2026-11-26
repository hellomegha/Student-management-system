from validation import *
from datetime import datetime
from storage import *
from database import add_student_db
students = []


def add_student():

    roll = get_valid_roll()

    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = get_valid_name()
    age = get_valid_age()
    student_class = input("Enter Class: ")
    marks = float(input("Enter Marks: "))
    gender = input("Enter Gender: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks,
        "gender": gender,
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    #students.append(student)
    add_student_db(student)
    
    save_data()
    print("Student added successfully!")


def view_students():

    if len(students) == 0:
        print("\nNo students found!\n")
        return

    print("\nTotal Students:", len(students))

    print("-" * 75)
    print(
        f"{'Roll':<10}{'Name':<20}{'Age':<10}"
        f"{'Class':<10}{'Marks':<10}{'Gender':<10}"
    )
    print("-" * 75)

    for student in students:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<10}"
            f"{student['class']:<10}"
            f"{student['marks']:<10.2f}"
            f"{student['gender']:<10}"
            f"{student['created_at']}"
        )

    print("-" * 75)

def search_student():
    keyword = input("Enter Roll Number to Search: ")

    

    for student in students:
         if (
        (keyword.isdigit() and student["roll"] == int(keyword))
        or (keyword.lower() in student["name"].lower())
    ):
            print("\nStudent Found:")
            print(f"Roll Number: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class']}")
            print(f"Marks: {student['marks']}")
            print(f"Gender: {student['gender']}")
            return

    print("Student not found!")



def delete_student():
    print("=== DELETE FUNCTION STARTED ===")

    roll = int(input("Enter Roll Number to Delete: "))

    for student in students:
        if student["roll"] == roll:

            print("Student found!")

            print("\nStudent to be deleted:")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")

            print("Before confirmation input")

            confirm = input("Are you sure? (Y/N): ")

            print("After confirmation input")
            print("You typed:", repr(confirm))

            if confirm.upper() == "Y":
                students.remove(student)
                save_data()
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found!")

def search_by_marks():

    minimum_marks = float(input("Enter Minimum Marks: "))

    found = False

    print("\nStudents with Marks >=", minimum_marks)
    print("-" * 50)

    for student in students:

        if student["marks"] >= minimum_marks:

            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Marks       : {student['marks']:.2f}")
            print("-" * 50)

            found = True

    if not found:
        print("No students found.")

def update_student():

    roll = get_valid_roll()

    for student in students:

        if student["roll"] == roll:

            print("\nCurrent Student Details")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Age         : {student['age']}")
            print(f"Class       : {student['class']}")
            print(f"Marks       : {student['marks']}")
            print(f"Gender      : {student['gender']}")

            print("\nEnter New Details")

            new_name = get_valid_name()

            confirm = input("Save Name? (Y/N): ")

            if confirm.upper() == "Y":
                student["name"] = new_name
                save_data()
                print("Name updated successfully!")
            else:
                print("Name update cancelled.")
            student["age"] = get_valid_age()
            student["class"] = input("Enter New Class: ")
            student["marks"] = float(input("Enter Marks: "))
            student["gender"] = input("Enter New Gender: ")

            print("\nStudent updated successfully!")
            return

    print("Student not found!")




