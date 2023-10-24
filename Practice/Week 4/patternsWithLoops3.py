#Pattern 3

"""
          1
        2 1
      3 2 1
    4 3 2 1
  5 4 3 2 1
6 5 4 3 2 1
"""

for i in range(1,7):
    for j in range(1,7-i):
        print(" ", end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()