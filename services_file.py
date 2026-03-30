import json # archivo tipo lista de diccionarios ordenada
import os # manejo de carpetas y archivos

CARPETA_DATA = "data"
ARCHIVO_JSON = os.path.join(CARPETA_DATA, "data.json") # ruta ára acceder al archivo json

# funtion reader
def read_data_students():
    # add all students in archivo json
    if not os.path.exists(ARCHIVO_JSON):
        return [] # return json vacio
    with open(ARCHIVO_JSON, 'r', encoding="utf-8") as f:
        return json.load(f) # return lista de diccionarios con la informacion de los estudiantes

def add_data_students(data_students):
    # add data this students in archivo json
    with open(ARCHIVO_JSON, 'w', encoding="utf-8") as f:
        json.dump(data_students, f, ensure_ascii=False, indent=4)

def create_data_student(data_student):
    # add new student
    data_students = read_data_students()
    data_students.append(data_student)
    add_data_students(data_students)

def update_data_student(name_value,name,add_new_student):
    # search and update data student
    data_students = read_data_students()
    for student in data_students:
        if student.get(name) == name_value:
            student.update(add_new_student)
            add_data_students(student)
            return True
    return False

def remove_data_student(name_value, name):
    # serach and remove data student
    data_students = read_data_students()
    update_data_students = []
    remove = False
    for student in data_students:
        if student.get(name) == name_value:
            remove = True
        else:
            update_data_students.append(student)
    if remove:
        add_data_students(update_data_students)
    
    return remove
