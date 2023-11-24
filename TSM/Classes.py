class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def setName(self, name):
        self.name = name
        return self.name
    
    def setPhone(self, phone):
        self.phone = phone
        return self.phone
      
      
class Product:
    def __init__(self, brand, model, desc, fails):
        self.brand = brand
        self.model = model
        self.desc = desc
        self.fails = fails
    
    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model
        
    def getDesc(self):
        return self.desc
    
    def getFails(self):
        return self.fails
        
    def setBrand(self, brand):
        self.brand = brand
        return self.brand
        
    def setModel(self, model):
        self.model = model
        return self.model
        
    def setDesc(self, desc):
        self.desc = desc
        return self.desc
    
    def setFails(self, fails):
        self.fails = fails
        return self.fails
    
    
class Client(Person):
    def __init__(self, name, phone, email, place):
        super().__init__(name, phone, email)
        self.place = place
        
    def getPlace(self):
        return self.place
        
    def setPlace(self, place):
        self.place = place
        return self.place


class Technician(Person):
    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        
        
class Ticket:
    def __init__(self, code, date, s_type):
        self.code = code
        self.date = date
        self.s_type = s_type
        
    def ctd(self, Client, Product, Technician):
        print("\n*-DATOS DE TICKET-*")
        print("Cód. Ticket:", self.code)
        print("Fecha del Ticket:", self.date.date())
        print("Cliente:", Client.name, "; Tlf:", Client.phone)
        print("Correo:", Client.email, "; Ubicación:", Client.place)
        print("Equipo:", Product.desc)
        print("Marca:", Product.brand, "; Modelo:", Product.model)
        print("Fallas que presenta:", Product.fails)
        print("Tecnico asignado:", Technician.name)
        print("Servicios a aplicar:", self.s_type)
        
        
class Service:
    inst_mntn = {1:"Instalacion Equipo", 2:"Instalacion S.O.",
                3:"Instalacion Software", 4:"Configuracion de equipos",
                5:"Actualizacion de equipos", 6:"Copia de Seguridad",
                7:"Resolucion Problemas Hardware", 8:"Resolucion Problemas Software"}
            
    support = {1:"Asistencia sobre Equipos", 2:"Asistencia sobre S.O.",
                3:"Asistencia sobre Software", 4:"Resolucion Problemas de Uso",
                5:"Formacion sobre Uso"}
        
    service_ctgs = {1:inst_mntn, 2:support}
    
    def selectServices(self):
        sel_active = True
        serv_list = []
        while sel_active:
            ctg_sel = int(input("""Elija la categoria del servicio:
    1) Instalacion/Mantenimiento
    2) Asistencia Tecnica
    Opcion: """))
            
            if ctg_sel == 1:
                serv_sel = int(input("""Elija el servicio a aplicar:
    1) Instalacion Equipo
    2) Instalacion S.O.
    3) Instalacion Software
    4) Configuracion de equipos
    5) Actualizacion de equipos
    6) Copia de Seguridad
    7) Resolucion Problemas Hardware
    8) Resolucion Problemas Software
    Opcion: """))
                service = self.inst_mntn.get(serv_sel)
                serv_list.append(service)
            
            elif ctg_sel == 2:
                serv_sel = int(input("""Elija el servicio a aplicar:
    1) Asistencia sobre Equipos
    2) Asistencia sobre S.O.
    3) Asistencia sobre Software
    4) Resolucion Problemas de Uso
    5) Formacion sobre Uso
    Opcion: """))
                service = self.support.get(serv_sel)
                serv_list.append(service)
                
            else:
                print("Servicio no existente")
            
            eos = str(input("Desea elegir otro servicio? s/n: "))
            if eos != 's':
                sel_active = False
            else:
                pass
        return serv_list
