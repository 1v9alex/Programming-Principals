# calculate the number of a factorial by using for loop

num = eval(input("Enter a number: "))
fact = 1
output = f"{num}! = "
for i in range(num, 0, -1):
    fact *= i
    output += str(i) + "*" if i > 1 else str(i) + " = "
output += str(fact)
print(output)