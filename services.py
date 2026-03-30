# ---- funtionalities sistem ------
from validations import *
from services_file import *

def add_new_student():
    data_students = read_data_students()

    id = validation_id()
    name = validation_name()
    age = validation_age()
    curso = validation_curso()
    status = validation_status()


    student ={
        "ID":id,
        "Name":name,
        "Age":age,
        "Curso":curso,
        "Status":status
    }
    icualyti = False

    for s in data_students:
        if s['ID'] == student['ID']:
            icualyti = True
            break
    if icualyti:
        print("\nOther student have this ID")
        return add_data_students()
    else:
        return student

def show_students():
    data_students = read_data_students()

    if len(data_students) == 0:
        print("\nnot have student")
    else:
        print("\n*** List Students ***")
        for i,s in enumerate(data_students):
            print(f"{i+1} - ID: {s['ID']} | Name: {s['name']} | Age: {s['age']} | Curso: {s['curso']} | Status: {s['status']}")

def search_student():
    # search for name
    name = validation_name()
    data_students = read_data_students()
    search = False
    for i,s in enumerate(data_students):
        if s['name'] == name:
            print(f"{i+1} - ID: {s['ID']} | Name: {s['name']} | Age: {s['age']} | Curso: {s['curso']} | Status: {s['status']}")
            search = True
            break
    return search

def update_student():
    name_value = validation_name()
    update_data_student(name_value,'name',add_new_student)


def remove_student():
    name_value = validation_name()
    remove_data_student(name_value,'name')