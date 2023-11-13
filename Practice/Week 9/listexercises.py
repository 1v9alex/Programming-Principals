#display the ints entered by the user in ascending order
#10 ints entered by the user

mylist = []

for x in range(0,10):
    mylist.append(int(input("Enter a number: ")))

mylist.sort()
print(mylist)

# now in descending order
mylist.sort(reverse=True)
print(mylist)