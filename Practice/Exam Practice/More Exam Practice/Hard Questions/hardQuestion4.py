"""
For Loops, Range & Conditional Statements: Use a for loop to print prime numbers between 2 and 50.
"""
import math

primeNumbers = []
flag = False

for num in range(2,51):
    flag = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            flag = False
            break
    if flag:
        primeNumbers.append(num)



print(primeNumbers)