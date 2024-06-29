a = int(input("Enter a = "))
b = int(input("Enter b = "))

try:
    print(f"{a} / {b} = {a/b}")

except ZeroDivisionError:
    print(f"{a} / {b} = infinite")

except Exception as e:
    print(e)