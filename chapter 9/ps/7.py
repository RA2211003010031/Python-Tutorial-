with open("chapter 9/ps/log.html", "r") as f:
    st = f.readlines()
print (st)
lineNumber = 1
for line in st:
    if("python" in line):
        print(f"Python found in line number {lineNumber}")
        break
    lineNumber+=1
else:
    print("Python not found in log file")