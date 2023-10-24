#Display 4 patterns using loops use nested loops to display the following patterns:

# Pattern 1
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''

for i in range(1,7):
    for j in range(1,i+1):
        print(j, end=" ")
    print() # add a new line after each row is printed