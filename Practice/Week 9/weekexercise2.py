#Read a collection fo words entered by the user, display each word entered by the user only once in the same order that the words were entered

mylist = []

for x in range(0,10):
    mylist.append(input("Enter a word: "))

# if the user add a word that is already in the list, do not add it again
#mylist = list(set(mylist))
#do it without using a set
newlist = []
for x in mylist:
    if x not in newlist:
        newlist.append(x)
mylist = newlist

print(mylist)