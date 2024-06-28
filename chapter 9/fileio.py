# f = open("test.txt")
# # text = f.readline()
# text = f.readlines()
# print(text)
# f.close()


# write->
# st = "Hey this is Adarsh Raj"
# f = open("chapter 9/writeFile.txt", "w")
# f.write(st)
# f.close()

with open("chapter 9/test.txt") as f:
    print(f.readlines())