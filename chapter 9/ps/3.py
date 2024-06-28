def generateTable(n):
    table = ""

    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"chapter 9/ps/tables/{n}thTable.txt", "w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)