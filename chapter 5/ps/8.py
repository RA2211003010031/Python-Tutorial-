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
if languages of 2 friends is same then....
Enter your name: raj
Enter your fav language: german
Enter your name: adarsh
Enter your fav language: english
Enter your name: shreya
Enter your fav language: german
Enter your name: manoj
Enter your fav language: hindi
result:
{'raj': 'german', 'adarsh': 'english', 'shreya': 'german', 'manoj': 'hindi'}
'''