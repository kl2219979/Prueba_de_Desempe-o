# ----- validation this values -----

def validation_id():
    # validation id
    try:
        id = int(input("Enter the ID this student:"))
        if id > 0:
            return str(id)
        else:
            print("\nInvalided ID, try again")
            return validation_id()
    except ValueError:
        print("Invalided ID")
        return validation_id()
    
def validation_age():
    # validation age
    try:
        age = int(input("Enter the Age this student:"))
        if age > 0 and age < 100:
            return age
        else:
            print("\nInvalided Age, try again")
            return validation_age()
    except ValueError:
        print("Invalided Age")
        return validation_age()

def validation_name():
    # valiation name
    name = input("Enter the Name this Student:").title()
    if name.strip().replace(" ","").isalpha():
        return name
    else:
        print("\nName invalided")
        return validation_name()

def validation_curso():
    # validation curso
    curso = input("Enter the Curso this Student -> mathematic(m), inglhis(i), chemestry(c):").lower()
    if curso == "m":
        return "mathematic"
    elif curso == "i":
        return "inglhis"
    elif curso == "c":
        return "chemestry"
    else:
        print("\nCurso invalided")
        return validation_curso()

def validation_status():
    # validation status
    status = input("Enter the status this Student -> activo(a), inactivo(i):")
    if status == "a":
        return "activo"
    elif status == "i":
        return "inactivo"
    else:
        print("\nStatus invalided")
        return validation_status()
    
