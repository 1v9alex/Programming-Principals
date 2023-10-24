a = "Canada is the best they have the  Canada best maple syrup and lots of landmarks like the CN tower and the rocky mountains"
b = "The United states is another good place to travel to they have the statue of liberty and the white house IS WORse then Canada"
c = "Mexico is a good place to travel to they have the mayan ruins and the pyramids worse then Canada and the United States"

q = input("Enter a single word search query: ").lower()
fa = a.lower().count(q)
fb = b.lower().count(q)
fc = c.lower().count(q)

if fa == 0 and fb == 0 and fc == 0:
    print("Sorry, no results found")
else:
    print("Here are the results:")
    if fa != 0:
        print("String 1:", a.count(q))
    if fb != 0:
        print("String 2:", b.count(q))
    if fc != 0:
        print("String 3:", c.count(q))
    print("Which result would you like to read?")
    if fa != 0:
        print("1. String 1")
    if fb != 0:
        print("2. String 2")
    if fc != 0:
        print("3. String 3")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(a)
    elif choice == 2:
        print(b)
    elif choice == 3:
        print(c)
    else:
        print("Invalid choice")