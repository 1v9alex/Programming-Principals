'''
Write a function that computes the sum of the digits in an integer. For
example, sumDigits(234) returns 9
'''

def sumDigits(num):
    counter = 0
    a = [int(i) for i in str(num)]
    for x in a:
        counter += x
    return counter

print(sumDigits(12345))