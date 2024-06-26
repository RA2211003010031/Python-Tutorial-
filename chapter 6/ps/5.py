name_list = ["adarsh", "shreya", "vatsh", "raj", "kumari"]

name = input("Enter the name to search: ")

if(name in name_list):
    print("Name found in the name list")
else:
    print("Name wasn't found in the name list")