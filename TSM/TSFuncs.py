from Classes import *
from datetime import datetime
import sqlite3 as sql3
import os

def createCode(ser_num):
    CODE = "TC"
    code = CODE + str(ser_num).rjust(4, "0")
    
    return code

def createTicket():
    selDb = str(input("Indique la base de datos a usar: "))
    if selDb[-3:] != ".db":
        selDb = selDb + ".db"
    t_num = 0
    service = Service()
    p_serv = ""

    c_name = str(input("Ingrese el Nombre del Cliente: "))
    c_phone = str(input("Ingrese el Telefono del Cliente: "))
    c_place = str(input("Ingrese la ubicacion del Cliente: "))
    c_email = str(input("Ingrese el correo del Cliente: "))
    p_desc = str(input("Ingrese la descripcion del equipo: "))
    p_brand = str(input("Ingrese la marca del equipo a revisar: "))
    p_model = str(input("Ingrese el Modelo del equipo a revisar: "))
    f_desc = str(input("Indique las fallas que presenta el equipo: "))
    services = service.selectServices()
    for service in services:
        p_serv = p_serv + service + " + "
    t_sel = stfDb(selDb)
    t_name = t_sel[0]
    t_phone = t_sel[1]
    t_email = t_sel[2]
    auto_rciDB(selDb, c_name, c_phone, c_place, c_email)
    auto_pciDB(selDb, p_brand, p_model, p_desc, f_desc)
    rtcDb(selDb, c_name, c_phone, c_email, p_brand, p_model, p_desc, f_desc, t_name)
    
    client = Client(c_name, c_phone, c_place, c_email)
    prod = Product(p_brand, p_model, p_desc, f_desc)
    tech = Technician(t_name, t_phone, t_email)
    t_code = auto_stcC(selDb)
    
    tck = Ticket(t_code, datetime.now(), p_serv)
    tck.ctd(client, prod, tech)

def auto_stcC(db_name):
    db_con = sql3.connect(db_name)
    tc_code_query = db_con.execute("SELECT tc_code FROM tickets")
    tc_codes = tc_code_query.fetchall()
    for codes in tc_codes:
        for code in codes:
            last_code = code
    return last_code

def stfDb(db_name):
    db_con = sql3.connect(db_name)
    t_name_query = db_con.execute("SELECT t_name FROM technician")
    t_names = t_name_query.fetchall()
    t_list = []
    for names in t_names:
        for name in names:
            t_list.append(name)

    for i in range(0, len(t_list)):
        print(i, "--", t_list[i])
    sel_tech = int(input("\nSegún el número,\nelija el técnico a asignar: "))
    tech = t_list[sel_tech]

    t_phone_query = db_con.execute(f"SELECT t_phone FROM technician WHERE t_name='{tech}'")
    t_phones = t_phone_query.fetchall()
    for phones in t_phones:
        tech_phone = phones[0]
        
    t_email_query = db_con.execute(f"SELECT t_email FROM technician WHERE t_name='{tech}'")
    t_emails = t_email_query.fetchall()
    for emails in t_emails:
        tech_email = emails[0]

    return tech, tech_phone, tech_email
    
def rtiDB():
    print("*-REGISTRO DE TECNICO-*")
    db_name = str(input("Ingrese el nombre de la base de datos: "))
    if db_name[-3:] != ".db":
        db_name = db_name + ".db"
    t_name = str(input("Ingrese el nombre del nuevo Tecnico: "))
    t_phone = str(input("Ingrese el número celular del tecnico: "))
    t_email = str(input("Ingrese el correo electronico del tecnico: "))
    tech_data = t_name, t_phone, t_email
    db_con = sql3.connect(db_name)
    db_new_data = db_con.execute(f"INSERT INTO technician(t_name, t_phone, t_email) VALUES{tech_data}")
    db_con.commit()
    print("REGISTRO REALIZADO CON ÉXITO")
    db_con.close()
    
def auto_rciDB(db, name, phone, place, email):
    client_data = name, phone, email, place
    db_con = sql3.connect(db)
    db_new_data = db_con.execute(f"INSERT INTO clients(c_name, c_phone, c_email, c_place) VALUES{client_data}")
    db_con.commit()
    db_con.close()
    
def rtcDb(db, cName, cPhone, cEmail, pBrand, pModel, pDesc, pFails, tName):
    ticket_data = 'TC000X', str(datetime.now()), cName, cPhone, cEmail, pBrand, pModel, pDesc, pFails, tName
    db_con = sql3.connect(db)
    db_new_data = db_con.execute(f"INSERT INTO tickets(tc_code, tc_date, c_name, c_phone, c_email, p_brand, p_model, p_desc, p_fails, t_name) VALUES{ticket_data};")
    db_con.commit()
    tcSysCode = db_con.execute("SELECT tc_sys_id FROM tickets;")
    tcNum = tcSysCode.fetchall()
    for num in tcNum:
        for n in num:
            tc_num_code = n
    tcCode = createCode(tc_num_code)
    db_rtcCode = db_con.execute(f"UPDATE tickets SET tc_code='{tcCode}' WHERE tc_sys_id={tc_num_code}")
    db_con.commit()
    db_con.close()
    
def auto_pciDB(db, brand, model, desc, fails):
    prod_data = brand, model, desc, fails
    db_con = sql3.connect(db)
    db_new_data = db_con.execute(f"INSERT INTO products(p_brand, p_model, p_desc, p_fails) VALUES{prod_data}")
    db_con.commit()
    db_con.close()

def cndb():
    print("*-CREACIÓN DE BASE DE DATOS-*")
    db_name = str(input("Ingrese el nombre de la BD: "))
    if db_name[-3:] != ".db":
        db_name = db_name + ".db"
    use_query = str(input("Desea usar un archivo SQL para crear las tablas? s/n: "))
    if use_query != 's':
        db_con = sql3.connect(db_name)
        db_con.close()
    else:
        filepath = str(input("Escriba la dirección exacta del archivo: "))
        with os.scandir(filepath) as fp:
            fp = [file.name for file in fp if file.is_file()
                  and file.name.endswith('.sql')]
        print("Archivos SQL disponibles:")
        for i in range(0, len(fp)):
            print([i], "--", fp[i])
        sel_file = int(input("\nSegún el número,\nelija el archivo a ejecutar: "))
        with open(filepath + fp[sel_file]) as sql_file:
            db_con = sql3.connect(db_name)
            try:
                db_con.execute(sql_file.read())
                print("Base de datos y tabla creada")
            except sql3.OperationalError:
                print("Ya existe esta tabla")
        
