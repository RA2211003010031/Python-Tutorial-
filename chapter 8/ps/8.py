def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

number = int(input("Enter the number: "))
table(number)