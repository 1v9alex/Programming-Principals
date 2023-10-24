"""
Data Types, Variables & Algorithms: Create a dictionary where keys are numbers between 1 and 5, and values are their respective factorials.
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_dict = {i: factorial(i) for i in range(1, 6)}

print(factorial_dict)
