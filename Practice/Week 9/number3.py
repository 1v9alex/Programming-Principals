#read a collection of ints from the user, display all the negative numbers followed by all of the zeros followed by all of the positive numbers
#put them in 3 separate lists

neglist = []
zerolist = []
poslist = []



for x in range(0,10):
    num = int(input("Enter a number: "))
    if num < 0:
        neglist.append(num)
    elif num == 0:
        zerolist.append(num)
    else:
        poslist.append(num)

print(neglist)
print(zerolist)
print(poslist)