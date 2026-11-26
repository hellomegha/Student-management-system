from student import *


def display_statistics():

    if len(students) == 0:
        print("\nNo students found!")
        return

    total_students = len(students)

    highest_marks = students[0]["marks"]
    lowest_marks = students[0]["marks"]
    total_marks = 0

    for student in students:

        total_marks += student["marks"]

        if student["marks"] > highest_marks:
            highest_marks = student["marks"]

        if student["marks"] < lowest_marks:
            lowest_marks = student["marks"]

    average_marks = total_marks / total_students

    print("\nSTUDENT STATISTICS")
    print("-" * 30)
    print(f"Total Students : {total_students}")
    print(f"Highest Marks  : {highest_marks:.2f}")
    print(f"Lowest Marks   : {lowest_marks:.2f}")
    print(f"Average Marks  : {average_marks:.2f}")
    print("-" * 30)


def get_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    else:
        return "D"
    

def student_report():

    roll = get_valid_roll()

    for student in students:

        if student["roll"] == roll:

            grade = get_grade(student["marks"])

            print("\n--------------------------------")
            print("       STUDENT REPORT")
            print("--------------------------------")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Class       : {student['class']}")
            print(f"Marks       : {student['marks']:.2f}")
            print(f"Grade       : {grade}")
            print("--------------------------------")

            return

    print("Student not found!")
