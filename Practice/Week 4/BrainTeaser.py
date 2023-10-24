#write program to input 3 numbers and find the maximum number without using the max function

a,b,c = input("Enter three numbers: ").split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)