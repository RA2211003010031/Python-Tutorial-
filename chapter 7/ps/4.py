number = int(input("Enter the number: "))

# for n in range(2,number-1):
#     if (number%n == 0):
#         print("Number is not prime")
#         break

if(number>1):
    prime = True
    for n in range(2,number-1):
        if(number%n == 0):
            prime = False
            break

    if(prime == True):
        print("Number is prime")
    else:
        print("Number is not prime")

else:
    print("Please enter the number greater than 2")