class Test:
    a = "0"
    
    def display(slf):
        print(f"a = {slf.a}")
    
obj1 = Test()
obj1.a = 2
obj1.display()
print(f"Value of Test a = {Test.a}")