import random

def game():
    score = random.randint(1,100)
    print(f"You got SCORE = {score}")
    return score

with open("hi-score.txt", "r") as f:
    highScore = f.read()
    if highScore!="":
        highScore = int(highScore)
    else:
        highScore = 0

score = game()
if(highScore < score):
    with open("hi-score.txt", "w") as f:
        f.write(str((score)))

else:
    pass