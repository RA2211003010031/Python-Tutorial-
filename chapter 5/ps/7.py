dictionary = {}

key = input("Enter your name: ")
value = input("Enter your fav language: ")
dictionary.update({key : value})
key = input("Enter your name: ")
value = input("Enter your fav language: ")
dictionary.update({key : value})
key = input("Enter your name: ")
value = input("Enter your fav language: ")
dictionary.update({key : value})
key = input("Enter your name: ")
value = input("Enter your fav language: ")
dictionary.update({key : value})

print(dictionary)


'''
if the name is same for 2 friends then...
Enter your name: adarsh
Enter your fav language: german
Enter your name: raj
Enter your fav language: english
Enter your name: adarsh
Enter your fav language: hindi
Enter your name: shreya
Enter your fav language: korean
result:
{'adarsh': 'hindi', 'raj': 'english', 'shreya': 'korean'}

the value taken at the last will be updated at the place of original value
'''