# comment = input("Enter the comment: ")

# comment = comment.lower()

# if(comment == "make a lot of money" or comment == "buy now" or comment == "subscribe this" or comment == "click this"):
#     print("Spam detected")
# else:
#     print("Spam not detected")


spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

comment = input("Enter the comment: ")

if ((spam1 in comment) or (spam2 in comment) or (spam3 in comment) or (spam4 in comment)):
    print("Spam comment found")
else:
    print("Spam comment not found")