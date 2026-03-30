# ---- funtionalities sistem ------
from validations import *

def add_new_student():
    id = validation_id()
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
    pass

def search_student():
    # buscar por id o nombre
    pass

def update_student():
    pass

def remove_student():
    pass