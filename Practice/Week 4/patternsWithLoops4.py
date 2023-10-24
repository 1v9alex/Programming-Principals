#Pattern 4

'''
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(1,7):
    for j in range(1,8-i):
        print(j, end=" ")
    print()