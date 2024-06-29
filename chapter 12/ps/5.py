
list1 = [1,2,3,4,5,6,7,8,9,10]
number = int(input("Enter the number: "))

list2 = [i for i in list1 if i%number==0]

with open("chapter 12/ps/tables.txt", "a") as f:
    f.write(str(list2) + "\n")