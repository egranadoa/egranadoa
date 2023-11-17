from Classes import *
from datetime import datetime

def createCode(ser_num):
    CODE = "TC"
    ser_num += 1
    code = CODE + str(ser_num).rjust(4, "0")
    
    return code

def createTicket():
    t_num = 0

    c_name = str(input("Ingrese el Nombre del Cliente: "))
    c_phone = str(input("Ingrese el Telefono del Cliente: "))
    c_place = str(input("Ingrese la ubicacion del Cliente: "))
    c_dni = str(input("Ingrese la identificacion del Cliente: "))
    p_desc = str(input("Ingrese la descripcion del equipo: "))
    p_brand = str(input("Ingrese la marca del equipo a revisar: "))
    p_model = str(input("Ingrese el Modelo del equipo a revisar: "))
    f_desc = str(input("Indique las fallas que presenta el equipo: "))
    p_serv = str(input("Especifique el tipo de servicio: "))
    t_name = str(input("Ingrese el Nombre del Tecnico a asignar: "))
    t_phone = "0414-0030025"
    t_code = createCode(t_num)

    client = Client(c_name, c_phone, c_place, c_dni)
    prod = Product(p_brand, p_model, p_desc)
    tech = Technician(t_name, t_phone)

    tck = Ticket(t_code, datetime.now(), p_serv, f_desc)
    tck.ctd(client, prod, tech)

def closeTicket(Client, Product, Technician, Ticket):
    print("\n*-FINALIZACION DE TICKET-*")