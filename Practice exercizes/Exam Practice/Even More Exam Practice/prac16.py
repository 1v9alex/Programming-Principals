"""
Write a function findHypot. 
The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. 
(Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
"""
import math

def findHypot(length1,length2):
    a = math.sqrt((length1**2)+(length2**2))
    return a


print(findHypot(1,2))