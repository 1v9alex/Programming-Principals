"""
Functions & Conditional Statements: Write a function that takes in two numbers and returns the larger. If they are equal, return "Equal".
"""

def largerNumber(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        return "Equal"

print(largerNumber(11,30))
print(largerNumber(40,10))
print(largerNumber(35,35))
