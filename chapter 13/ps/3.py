# JOIN METHOD (STRINGS) 
# Creates a string from iterable objects. 
# l = ["apple", "mango", "banana"] 
# result = ", and, ".join(l) 
# print(result) 
# The above line will return “apple,and,mango,and,banana”.

table = [str(7*i) for i in range(1,11)]

result = "\n".join(table)
print(result)