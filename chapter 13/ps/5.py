# Reduce applies a rolling computation to sequential pair of elements. 
# from functools import reduce 
# val=reduce (function, list1)        
# # the function can be lambda function 

from functools import reduce


def max(a,b):
    if(a>b):
        return a
    return b

li = [1,2,3,4,5,6,7,8,7,5,4,53,23,25,34,32,423,4]

print(reduce(max, li))

