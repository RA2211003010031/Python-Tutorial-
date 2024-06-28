class Programmer:
    name = ""
    age = ""
    dept = ""
    lang = ""

    def __init__(self,name,age,dept,lang):
        self.age = age
        self.dept = dept
        self.lang = lang
        self.name = name
        
    def printDetails(self):
        print(f"Name = {self.name}\nAge = {self.age}")
    
prog1 = Programmer("Adarsh", 22, "SDE", "py")
prog2 = Programmer("Shreya", 19, "Designer", "HTML")

prog1.printDetails()
prog2.printDetails()