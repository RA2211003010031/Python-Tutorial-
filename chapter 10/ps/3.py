class Test:
    a = "0"
    
    def display(self):
        print(f"a = {self.a}")
    
obj1 = Test()
obj1.a = 2
obj1.display()
print(f"Value of Test a = {Test.a}")