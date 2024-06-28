censoredWords = ["donkey", "ganda", "bura", "gadha"]

with open("chapter 9/ps/4Donkey.txt", "r") as f:
    st = f.read()
    
for word in censoredWords:
    st = st.replace(word, "#" * len(word))

with open("chapter 9/ps/4Donkey.txt", "w") as f:
    f.write(st)