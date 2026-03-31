# ---- funtionalities sistem ------
from validations import *
from services_file import *

def add_new_student():
    # funtion add new studen 
    data_students = read_data_students()

    id = validation_id()
    for s in data_students:
        if s['ID'] == id:
            print("\nOther student have this ID")
            return add_new_student()

    name = validation_name()
    age = validation_age()
    curso = validation_curso()
    status = validation_status()


    return {
        "ID":id,
        "Name":name,
        "Age":age,
        "Curso":curso,
        "Status":status
    }
    
    
def show_students():
    # funtion show all students
    data_students = read_data_students()

    if len(data_students) == 0:
        print("\nnot have student")
        return
    else:
        print("\n*** List Students ***")
        for i,s in enumerate(data_students):
            print(f"{i+1} - ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Curso: {s['Curso']} | Status: {s['Status']}")

def search_student():
    # funtion search studen with name
    data_students = read_data_students()

    if len(data_students) == 0:
        print("\nnot have student")
        return
    # search for name
    name = validation_name()
    data_students = read_data_students()
    search = False
    for i,s in enumerate(data_students):
        if s['Name'] == name:
            print(f"{i+1} - ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Curso: {s['Curso']} | Status: {s['Status']}")
            search = True
            break
    return search

def update_student():
    # funtion update student with name
    data_students = read_data_students()
    if len(data_students) == 0:
        print("\nnot have student")
        return
    name_value = validation_name()
    update = update_data_student(name_value)

    if update:
        print("update corretly")
    else:
        print("Not can update")

    


def remove_student():
    # funtion remove student with name
    data_students = read_data_students()

    if len(data_students) == 0:
        print("\nnot have student")
        return
    name_value = validation_name()
    remove_data_student(name_value)