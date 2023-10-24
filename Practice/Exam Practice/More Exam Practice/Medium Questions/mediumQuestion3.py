"""
While Loops & Range: Use a while loop to simulate a dice roll (numbers 1-6) until a 5 is rolled.
"""
import random

num = random.randint(1,6)
print(num)
while num != 5:
    num = random.randint(1,6)
    print(num)

