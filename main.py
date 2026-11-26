from validation import *
from storage import *
from student import *
from reports import *
from database import create_table

def display_menu():

    print("\nSTUDENT MANAGEMENT SYSTEM")
   # print("-----------------------------")
    print("NEW VERSION LOADED")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Search Students by Marks")
    print("7. Update Student")
    print("8. Display Statistics")
    print("9. Student Report")
    print("10. Export Backup")
def main():
    
    create_table()
    load_data()
    while True:

        display_menu()

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Thank you for using the system!")
            break
       
        elif choice == "4":
            search_student()
            

        elif choice == "5":
            delete_student()

        elif choice == "6":
            search_by_marks()

        elif choice == "7":
            update_student()

        elif choice == "8":
            display_statistics()

        elif choice == "9":
            student_report()

        elif choice == "10":
            export_backup()

        else:
            print("Invalid Choice!")


main()