"""
Data Types, Selection & Loops: Ask the user to input a list of numbers and then print the sum of even numbers in the list.
"""

numberList = []
amountOfNumbers = int(input("Enter number of elements in the list: "))
totalSum = 0
evenNumberList = []

for i in range(0,amountOfNumbers):
    userNumbers = int(input("Enter a number: "))
    
    numberList.append(userNumbers)


for num in numberList:
    if num % 2 == 0:
        totalSum += num
        
evenNumberList.append(totalSum)

print(evenNumberList)