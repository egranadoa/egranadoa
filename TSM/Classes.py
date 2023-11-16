class Person:
    def __init__(self, name, phone, place):
        self.name = name
        self.phone = phone
        self.place = place
    
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def getPlace(self):
        return self.place
    
    def setName(self, name):
        self.name = name
        return self.name
    
    def setPhone(self, phone):
        self.phone = phone
        return self.phone
    
    def setName(self, place):
        self.place = place
        return self.place
    
    
class Client(Person):
    def __init__(self, name, phone, place):
        super().__init__(name, phone, place)
