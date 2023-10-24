"""
Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime number and False otherwise.
"""

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True
        
print(isPrime(110))


print('p' in 'pineapple')