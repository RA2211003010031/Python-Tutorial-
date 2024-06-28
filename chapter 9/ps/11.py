# old file name = rename.txt

with open("chapter 9/ps/rename.txt", "r") as f:
    content = f.read()

with open("chapter 9/ps/renamed.txt", "w") as f:
    f.write(content)
    
