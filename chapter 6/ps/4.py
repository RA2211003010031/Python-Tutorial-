username = input("Enter the username: ")

count = len(username)
print("Count = ", count)

if count<10:
    print("Less than 10 characters found")
else:
    print("More than or equal to 10 characters found")