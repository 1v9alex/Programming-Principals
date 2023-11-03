def sort(n1,n2,n3):
    if n1>n2 and n1>n3 and n2>n3:
        return n3,n2,n1
    elif n1>n2 and n1>n3 and n3>n2:
        return n2,n3,n1
    elif n2>n1 and n2>n3 and n1>n3:
        return n3,n1,n2
    elif n2>n1 and n2>n3 and n3>n1:
        return n1,n3,n2
    elif n3>n1 and n3>n2 and n1>n2:
        return n2,n1,n3
    elif n3>n1 and n3>n2 and n2>n1:
        return n1,n2,n3
    else:
        return n1,n2,n3
    

print(sort(1,2,3))
print(sort(n1=2,n2=3,n3=1))
print(sort(3,n2=3,n3=1))
#print(sort(n1=4,n2=3,1))