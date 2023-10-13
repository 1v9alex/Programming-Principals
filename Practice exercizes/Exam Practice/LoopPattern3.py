for i in range(1,7):
    for x in range(1,7-i):
        print(" ", end= " ")
    for x in range(i,0,-1):
        print( x, end =" ")
    print()