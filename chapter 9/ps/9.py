with open("chapter 9/ps/file9.1.txt", "r") as f:
    st1 = f.readlines()
with open("chapter 9/ps/file9.2.txt", "r") as f:
    st2 = f.readlines()

if(st1 == st2) :
    print("Same files")
else:
    print("Not same files")