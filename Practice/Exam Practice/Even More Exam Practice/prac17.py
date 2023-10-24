"""
Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.
"""

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(isEven(2))


"""
Now write the function is_odd(n) that returns True when n is odd and False otherwise.

"""

def isOdd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
print(isOdd(2))


"""
Modified isOdd function
"""
def isOdd(n):
    if isEven(n):
        return False
    else:
        return True
print(isOdd(7))