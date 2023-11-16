class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
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
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model
        
    def setBrand(self, brand):
        self.brand = brand
        return self.brand
        
    def setModel(self, model):
        self.model = model
        return self.model
    
    
class Client(Person):
    def __init__(self, name, phone, place):
        super().__init__(name, phone)
        self.place = place
        
    def getPlace(self):
        return self.place
        
    def setPlace(self, place):
        self.place = place
        return self.place


class Technician(Person):
    def __init__(self, name, phone):
        super().__init__(name, phone)
