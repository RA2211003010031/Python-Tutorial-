# FORMAT METHOD (STRINGS) 
# Formats the values inside the string into a desired output. 
# template.format(p1,p2...) 
# Syntax: 
# "{} is a good {}".format("harry", "boy")   #1. 
# "{} is a good {o}".format("harry", "boy")  #2. 
# # output for 1: 
# # harry is a good boy  
# # output for 2: 
# # boy is a good harry 


name = input("Enter your name : ")
marks = input("Enter your marks : ")
phoneNo = input("Enter your phone no : ")

print("The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phoneNo))