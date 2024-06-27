def celToFah(cel):
    fah = ((9/5)*cel)+32
    return fah

tempinCel = int(input("Enter the temperature in celsius: "))
print(f"{tempinCel} Deg celsius = {celToFah(tempinCel)} Deg fahrenhite")