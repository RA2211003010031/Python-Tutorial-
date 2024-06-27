def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
    
num1 = 10
num2 = 100
num3 = 20

print(f"The greatest of {num1}, {num2} and {num3} is {greatest(num1,num2,num3)}")