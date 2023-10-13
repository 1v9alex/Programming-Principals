total = 0.0
total2 = 1.0

num = 0

num = eval(input("Enter A Number "))

for i in range(1, num+1):
    total += 1/i
    total2 *= i
    
print(total)
print(total2)