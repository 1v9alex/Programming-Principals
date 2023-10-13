
negCounter = 0
average = 0
total = 0
posCounter = 0

num = -1


while num != 0:
    num = int(input("Enter a number, input 0 to exit: "))
    total += num
    if num > 0:
        posCounter += 1
    elif num < 0:
        negCounter += 1

print(total)
average = total / (negCounter+posCounter)
print(average)
