"""
Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled.
Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality.
If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as
"""

import math

def is_rightangled(a,b,c):
    if math.sqrt((c**2)) == math.sqrt((a**2)+(b**2)):
        return True
    elif math.sqrt((b**2)) == math.sqrt((a**2)+(c**2)):
        return True
    elif math.sqrt((a**2)) == math.sqrt((b**2)+(c**2)):
        return True
    else:
        return False
    

def is_rightangled(a, b, c):
    return a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2


print(is_rightangled(10,304,123))


def is_rightangled(a, b, c):
    sides = sorted([a, b, c])
    return sides[2]**2 == sides[0]**2 + sides[1]**2

print(is_rightangled(10, 304, 123))
