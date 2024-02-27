from Classes import *
import psycopg2
import getpass

def checkStudentsFromDb(db_name, db_host, db_user, db_pass, db_port):
    conn = psycopg2.connect(database=db_name,
                            host=db_host,
                            user=db_user,
                            password=db_pass,
                            port=db_port)

    cursor = conn.cursor()


    cursor.execute("SELECT usuarios.id, usuarios.nombre, usuarios.apellido, usuarios.cedula, usuarios.nacionalidad, usuarios.tipo FROM usuarios WHERE usuarios.tipo=3;")
    usr_data = cursor.fetchall()
    cursor.execute("SELECT estudiantes.trayecto, estudiantes.semestre, estudiantes.carrera, estudiantes.usuario FROM estudiantes;")
    std_data = cursor.fetchall()
    cursor.execute("SELECT carrera.id, carrera.nombre FROM carrera;")
    crr_data = cursor.fetchall()
    conn.close()

    std_list = []

    for i in range(len(usr_data)):
        if usr_data[i][0] == std_data[i][3] and usr_data[i][5] == 3:
            for j in range(len(crr_data)):
                if usr_data[i][0] == std_data[i][3] and crr_data[j][0] == std_data[i][2]:
                    valid_student = Student(usr_data[i][1], usr_data[i][2],
                                            usr_data[i][3], usr_data[i][4],
                                            crr_data[j][1], std_data[i][0],
                                            std_data[i][1])
                    std_list.append(valid_student)
            
    for student in std_list:
        student.getInfo()


