with open("chapter 9/ps/log.html") as f:
    st = f.read()

if ("python" in st):
    print("Python found")
else:
    print("Python not found")