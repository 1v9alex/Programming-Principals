"""
Modules, For Loops & Variables: Use the random module to simulate the roll of two dice 10 times, and store the results in a list.
"""
import random

emptyList = []

for i in range(0,10):
    emptyList.append(random.randint(2,12))

print(emptyList)