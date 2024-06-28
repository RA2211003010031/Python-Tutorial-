class Employee:
    salary = 10000
    language = "py"
    
    def __init__(self): #this is called dunder method and is called automatically
        print("Creating the object for Employee class")

    def display(self):
        print(f"{self.name} has salary of {self.salary} and is working in {self.language} language")
    
    @staticmethod #used if the methods below isn't using any objects whether its instance or class 
    def greet():
        print("Good morning Dear!")

adarsh = Employee()
adarsh.name = "Adarsh Raj"
adarsh.display()
adarsh.greet()