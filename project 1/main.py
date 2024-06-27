# PROJECT  1: SNAKE, WATER, GUN GAME

'''
snake = 1
water = 2
gun = 3
 
The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
'''

import random

computerStr  = random.choice([-1,0,1])

youStr = int(input("Enter your choice: "))

choiceDict = {
    -1 : "Snake",
    0 : "Water",
    1 : "Gun"
}

you = choiceDict[youStr]
computer = choiceDict[computerStr]

print(f"Computer choosed {computer}\nYou choosed {you}")

if computerStr == youStr:
    print("It's a draw!")

else:
    if(computerStr == -1 and youStr == 1):
        print("You win!")
    
    elif(computerStr == -1 and youStr == 0):
        print("You lose!")
    
    elif(computerStr == 1 and youStr == -1):
        print("You lose!")
    
    elif(computerStr == 1 and youStr == 0):
        print("You win!")
    
    elif(computerStr == 0 and youStr == -1):
        print("You win!")
    
    elif(computerStr == 0 and youStr == 1):
        print("You lose!")
    
    else:
        print("Something went wrong!")