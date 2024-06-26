letter = '''Dear <|Name|>, 
                You are selected! 
                <|Date|>''' 

name = input("Enter the name: ")
date = input("Enter the date: ")

# chaining

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))