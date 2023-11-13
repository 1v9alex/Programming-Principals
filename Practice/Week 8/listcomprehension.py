for x in range(1,10):
    print(x)

# do with list comprehension
mylist = [x for x in range(1,10)]

#lis tcomprehension to find only items having cost more than 30

cost = [10,30,40,20,40,60,20]

#filter based on the cost lsit
items = [x for x in cost if x > 30]
print(items)


#write a list comprehension for item    