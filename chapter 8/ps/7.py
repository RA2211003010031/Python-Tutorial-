def remove(li,st) :
    n = []

    for item in li:
        if (item != st):
            n.append(item.strip(st))
    return n


li = ["Adarshan", "Shreyaan", "Manojan", "an"]
print(remove(li,"an"))