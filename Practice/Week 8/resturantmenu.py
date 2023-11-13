mylist = ["coffe","egg sandwich","muffin"]

userOrder = input("What would you like to order? ")

if userOrder in mylist:
    print("Your order is being prepared")
else:
    print("Your order is not on the menu")