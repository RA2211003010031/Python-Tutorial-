try:
    with (
        open("chapter 12/ps/1.txt", "r") as f1,
        open("chapter 12/ps/2.txt", "r") as f2,
        open("chapter 12/ps/3.txt", "r") as f3 
    ):
        st1 = f1.read()
        st2 = f2.read()
        st3 = f3.read()

except Exception as e:
    print("We aren't able to read a file")
    print(e)