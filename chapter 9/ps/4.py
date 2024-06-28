# st = "this is donkey word, here also a donkey"

# if("donkey" in st):
#     st= st.replace("donkey", "#####")

# print(st)

with open("chapter 9/ps/4Donkey.txt", "r") as f:
    st = f.read()

# if "donkey" in st:
#     st = st.replace("donkey", "#####")
#     print("Replacing done!")

st = st.replace("donkey", "#####")

with open("chapter 9/ps/4Donkey.txt", "w") as f:
    f.write(st)