# --------- Menu --------------------
from services import *
from services_file import create_data_student

def menu():
    while True:
        print("\n*** WELCOME SISTEM MANAGER STUDENTS ***")
        print("1.Add student")
        print("2.Show students")
        print("3.Serach students")
        print("4.update student")
        print("5.Remove student")
        print("6.Exit")
        option = input("Enter your option:")
        match option:
            case '1':
                data_student = add_new_student()
                create_data_student(data_student)
            case '2':
                show_students()
            case '3':
                search_student()
            case '4':
                update_student()
            case '5':
                remove_student()
            case '6':
                print("Exit this program ...")
                break
            case _:
                print("option invalided")