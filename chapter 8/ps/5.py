def printStar(n):
    for i in range(0,n+1):
        print("*"*(n-i), end="")
        print("")

n = 3
printStar(3)