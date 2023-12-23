from fpdf import FPDF

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
    def __init__(self, code, date):
        self.code = code
        self.date = date
        
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
        
        
class Services:
    def prod_rec(self, c_name, c_phone, c_email, p_brand, p_model, p_desc, f_desc, t_name, t_phone, t_email, tc_code):
        new_bill = TSM_Bill_Reception('P', 'mm', 'Letter')
        new_bill.add_page()
        new_bill.set_font('helvetica', 'B', 14)
        new_bill.cell(new_bill.w, 5, 'Datos del Cliente', 0, 1, 'L')
        new_bill.ln(5)
        new_bill.Client_Data(c_name, c_phone, c_email, p_brand, p_model, p_desc, f_desc)
        new_bill.set_font('helvetica', 'B', 14)
        new_bill.cell(new_bill.w, 5, 'Datos del Técnico', 0, 1, 'L')
        new_bill.ln(5)
        new_bill.Tech_Data(t_name, t_phone, t_email)
        new_bill.set_font('helvetica', 'B', 14)
        new_bill.cell(new_bill.w, 5, f'Ticket Asignado: {tc_code}', 0, 1, 'L')
        new_bill.ln(5)
        new_bill.output('test_rec_bill.pdf')


class TSM_Bill_Reception(FPDF):
    def header(self):
        title = 'Recepción de Equipo(s)'
        self.set_margins(25.4, 25.4)
        self.set_font('helvetica', 'B', 18)
        title_w = self.get_string_width(title) + 4
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 10, title, border=0, ln=1, align='C', fill=0)#habilitar fondos y bordes
        self.ln(10)
        
    def Client_Data(self, c_name, c_phone, c_email, p_desc, p_brand, p_model, f_desc):
        self.set_font('helvetica', '', 12)
        self.cell(self.w, 5, f'Nombre: {c_name}', 0, 1, 'L')
        self.cell(self.w, 5, f'Teléfono: {c_phone}', 0, 1, 'L')
        self.cell(self.w, 5, f'Correo: {c_email}', 0, 1, 'L')
        self.cell(self.w, 5, f'Tipo de Equipo revisado: {p_desc}', 0, 1, 'L')
        self.cell(self.w, 5, f'Marca del Equipo: {p_brand}', 0, 1, 'L')
        self.cell(self.w, 5, f'Modelo del Equipo: {p_model}', 0, 1, 'L')
        self.cell(self.w, 5, f'Fallas especificadas: {f_desc}', 0, 1, 'L')
        self.ln(15)
    
    def Tech_Data(self, t_name, t_phone, t_email):
        self.set_font('helvetica', '', 12)
        self.cell(self.w, 5, f'Nombre: {t_name}', 0, 1, 'L')
        self.cell(self.w, 5, f'Teléfono: {t_phone}', 0, 1, 'L')
        self.cell(self.w, 5, f'Correo: {t_email}', 0, 1, 'L')
        self.ln(15)
        
    
