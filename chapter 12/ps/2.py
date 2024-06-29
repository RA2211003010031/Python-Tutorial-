# ENUMERATE FUNCTION IN PYTHON  
# The ‘enumerate’ function adds counter to an iterable and returns it
# for index, item in enumerate(l):
#   print(f"The item number at index {index} is {item}")

li = [0,1,2,3,4,5,6,7,8,9,10]

for index, item in enumerate(li):
    if(index == 3) or (index == 5) or (index == 7):
        print(f"Element at index {index} is {item}")
    else:
        continue