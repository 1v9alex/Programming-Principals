#write a function called average that takes a list of numbers as a parameter and returns the average of the numbers

def average(mylist):
    total = 0
    for x in mylist:
        total += x
    return total / len(mylist)

print(average([1,2,3,4,5,6,7,8,9,10]))