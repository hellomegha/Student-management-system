import json
import os


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Data saved successfully!")
    display_file_size()

def display_file_size():
    try:
        size = os.path.getsize("students.json")  
        size_kb = size / 1024                    
        print(f"Data File Size: {size_kb:.2f} KB")
    except FileNotFoundError:
        print("students.json file does not exist.")


def load_data():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print(f"Loaded {len(students)} students Records Loaded")

    except FileNotFoundError:
        students = []
        print("No Existing Data Found.")

    except json.JSONDecodeError:

        print(
        "Data File Corrupted."
    )

    students = []


def export_backup():

    with open(
        "students_backup.json",
        "w"
    ) as file:

        json.dump(
            students,
            file,
            indent=4
        )

    print(
        "Backup Created Successfully."
    )

def import_backup():

    try:
        with open(
            "students_backup.json",
            "r"
        ) as file:

            global students
            students = json.load(file)

        save_data()
        print(
            "Backup Imported Successfully."
        )

    except FileNotFoundError:
        print(
            "No Backup Found."
        )