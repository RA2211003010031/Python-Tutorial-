with open("chapter 9/ps/this.txt", "r") as f:
    st1 = f.read()

with open("chapter 9/ps/this_copy.txt", "w") as f:
    f.write(st1)