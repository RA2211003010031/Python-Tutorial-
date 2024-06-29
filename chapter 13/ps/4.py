# Filter creates a list of items for which the function returns true. 
# list(filter(function)) 
# # the function can be lambda function

def div5(n):
    if(n%5 == 0):
        return True
    return False

li = [1,2,3,4,5,6,7,8,9,10,12,14,15,17,19,20]

result = list(filter(div5,li))

print(result)