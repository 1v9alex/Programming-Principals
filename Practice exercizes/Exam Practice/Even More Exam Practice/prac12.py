"""Use a for statement to print 10 random numbers.
Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.
"""

import random

for i in range(0,10):
    print(random.randint(25,35))