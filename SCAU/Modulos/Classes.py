

class Student:
    def __init__(self, name, surname, idc, nation, carreer, course, sem):
        self.name = name
        self.surname = surname
        self.idc = idc
        self.nation = nation
        self.carreer = carreer
        self.course = course
        self.sem = sem

    def getInfo(self):
        print("---\nNombre:", self.name, "\nApellido:", self.surname, "\nCédula:",
              self.idc, "\nNacionalidad:", self.nation, "\nCarrera:",
              self.carreer, "Trayecto cursando:", self.course, "\nSemestre:",
              self.sem, "\n---")
        
