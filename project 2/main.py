#                                       PROJECT 2  – THE PERFECT GUESS 

# import random

# def start():
#     print("LET'S START THE GAME: THE PERFECT GUESS\n")

# def randomNumber():
#     return random.randint(1,100)

# def compare(original, n):
#     if(original<n):
#         print("Lower number please")
#     else:
#         print("Higher number please")    

# start()
# number = randomNumber()
# print(f"Random number Generated: {number}")
# guess = 0

# playerNo = int(input("Enter your guess: "))
# if(number == playerNo):
#     print("\nYou have successfully guessed the number in only 1 try.!\n")

# else:
#     compare(number,playerNo)
#     while(playerNo != number):
#         playerNo = int(input("Enter your guess: "))
#         guess+=1
#         if(number == playerNo):
#             print(f"\nYou guessed the number in {guess} tries..!")
#             break
#         else:
#             compare(number,playerNo)

# print("\n\t--> GAME END <--\n\n")


from random import randint

originalNumber = randint(1,100)
print(f"Original number generated is {originalNumber}")

a = -1
guesses = 0

while (a!=originalNumber):
    a = int(input("Enter your guess: "))
    guesses+=1
    if(a<originalNumber):
        print("Guess higher number..!")
    elif(a>originalNumber):
        print("Guess Lower Number..!")

print(f"You have successfully guessed the number {originalNumber} in {guesses} guess....")