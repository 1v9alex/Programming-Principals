#creatre a list called mylist with the following 6 items , 76,92.3,"hello",True,4,76 
#then write a list comprehension that creates a list of only the int items in mylist

mylist = [76,92.3,"hello",True,4,76]

newlist = [x for x in mylist if type(x) == int]
print(newlist)

