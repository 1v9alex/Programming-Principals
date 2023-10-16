"""
Algorithms, Selection & Iteration: Write a program that finds the second largest number in a given list of numbers.
"""

numList = [4000,4001,1,2,3,4,5,6,3495,39458]
secondLargest = 0
largest = 0

for i in numList:
    if i > largest:
        secondLargest = largest
        largest = i
    elif i > secondLargest and i != largest:
        secondLargest = i

print(secondLargest)