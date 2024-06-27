def sumN(n):
    if(n==1):
        return 1
    return sumN(n-1)+n

n = 3
print(f"The sum = {sumN(n)}")

