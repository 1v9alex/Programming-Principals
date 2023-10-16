"""
Functions, For Loops & Algorithms: Write a function that computes the factorial of a given number using a for loop.
"""

def findFactorial(num):
    factorial = 1
    for i in range(1,num+1):
       # print(i)
        factorial *= i
    return factorial

print(findFactorial(10))
print(findFactorial(2))
print(findFactorial(5))