from Classes import *
from TSFuncs import *

program_active = True
print("TechnicalSupportManagement".center(52, "*"))
print("Version 0.1".center(52, "-"))

while program_active:
    menu_sel = int(input("""1) Crear Ticket
2) Registrar Técnico
3) Crear BD/Tablas
Opción: """))
    if menu_sel == 1:
        createTicket()
    elif menu_sel == 2:
        rtiDB()
    elif menu_sel == 3:
        cndb()
    else:
        print("Opción no disponible")
    eos = str(input("Desea volver a usar el programa? s/n: "))
    if eos != 's':
        program_active = False
    else:
        pass
