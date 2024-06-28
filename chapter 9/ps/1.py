'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. 
'''

with open("chapter 9/ps/poems.txt") as f:
    text = f.read()
    
if ("twinkle" in text):
    print("Twikle found")
else:
    print("Not found")