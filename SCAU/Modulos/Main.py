from pgdb_test import *

program_active = True
print("Módulo de Constancias de Estudios".center(62, "*"))
print("Version 0.1.0".center(62, "-"))

while program_active:
    db_name = str(input('Escriba el nombre de la Base de Datos: '))
    db_host = str(input('Escriba la dirección del servidor: '))
    db_user = str(input('Escriba el usuario para la BD PostgreSQL: '))
    db_pass = getpass.getpass('Escriba la contraseña: ')
    db_port = str(input('Escriba el puerto de conexión a la BD: '))

    menu_sel = int(input("""1) Consultar información de Estudiantes
2) Generar Constancia de Estudios
Opción: """))
    if menu_sel == 1:
        checkStudentsFromDb(db_name, db_host, db_user, db_pass, db_port)
    elif menu_sel == 2:
        createStudiesCert(db_name, db_host, db_user, db_pass, db_port)
    else:
        print("Opción no disponible")
    eos = str(input("Desea volver a usar el programa? s/n: "))
    if eos != 's':
        program_active = False
    else:
        pass
