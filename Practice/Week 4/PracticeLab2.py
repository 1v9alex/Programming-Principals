a, b, c = input("Enter 3 numbers separated by commas: ").split(",")
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    if b > c:
        print("Maximum number:", a)
        print("Second largest number:", b)
    else:
        print("Maximum number:", a)
        print("Second largest number:", c)
elif b > a and b > c:
    if a > c:
        print("Maximum number:", b)
        print("Second largest number:", a)
    else:
        print("Maximum number:", b)
        print("Second largest number:", c)
else:
    if a > b:
        print("Maximum number:", c)
        print("Second largest number:", a)
    else:
        print("Maximum number:", c)
        print("Second largest number:", b)