# LIST COMPREHENSIONS  
# List Comprehension is an elegant way to create lists based on existing lists. 
# list1 = [1,7,12,11,22,] 
# list2 = [i for item in list 1 if item > 8] 


list1 = [1,2,3,4,5,6,7,8,9,10]
number = int(input("Enter the number: "))

list2 = [i for i in list1 if i%number==0]
print(list2)