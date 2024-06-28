import math as m

class Calculator:

    def square(self,n):
        print(f"The square of {n} is {n*n}")
    
    def cube(self,n):
        print(f"The cube of {n} is {n*n*n}")

    def sqRoot(self,n):
        print(f"The square of {n} is {m.sqrt(n)}")
        
num1 = Calculator()
num1.sqRoot(36)
num1.cube(36)
num1.square(36)