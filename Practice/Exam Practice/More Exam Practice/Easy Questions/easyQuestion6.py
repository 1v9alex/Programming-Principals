"""
Selection & Conditional Statements: Given a list of numbers, use a loop to find and print the first negative number.
"""

numList = [1,-2,3,-4,5,6,7]

negStored = 0
for n in numList:
    if n < 0:
        negStored = n
        break

if negStored != 0:
    print(negStored)
elif negStored == 0:
    print("There Are No Negative numbers in this list")