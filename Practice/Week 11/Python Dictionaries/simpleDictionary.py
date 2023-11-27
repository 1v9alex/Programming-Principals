dict = {}

print(type(dict))

subjects = {"Math": 100, "English": 90, "Science": 80}



#use loop with range fucntion to ask the user for 5 subjects and their marks and add to the dict

for i in range(1):
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))
    subjects[subject] = mark
    
print(subjects)

#print they keys of the dict
print(subjects.keys())

#print the values of the dict
print(subjects.values())

#print the items of the dict
print(subjects.items())



v1 = subjects.get("Health",0)


# Find the subject with the highest mark
highest_mark_subject = max(subjects, key=subjects.get)
print(f"Your highest mark was a {subjects[highest_mark_subject]} in {highest_mark_subject}")

# Find the subject with the lowest mark
lowest_mark_subject = min(subjects, key=subjects.get)
print(f"Your lowest mark was a {subjects[lowest_mark_subject]} in {lowest_mark_subject}")

#put in a list

lvals = list(subjects.values())


#check if key in dict

if "Math" in subjects:
    print("Math is in the dict")
else:
    print("Math is not in the dict")


#calculate the avergae mark and print it
average = sum(subjects.values())/len(subjects)
print(f"Your average mark is {average}")


#create a resturant menu using dictionaries 

menu = {"Chicken": 10, "Beef": 15, "Pork": 12, "Fish": 20, "Vegetarian": 8,"Churro":3}
drinkMenu = {"Coke": 2, "Sprite": 2, "Water": 1, "Orange Juice": 3, "Apple Juice": 3, "Milk": 2}

print(menu)

#add a new item to the menu
menu["Duck"] = 25

print(menu)

#remove an item from the menu
del menu["Fish"]

print(menu)

#change the price of an item

menu["Chicken"] = 12

print(menu)

#ask the user for an item and print the price

item = input("Enter an item: ")

if item in menu:
    print(f"The price of {item} is {menu[item]}")
else:
    print(f"{item} is not in the menu")

#allow them to order a drink first based on number of guests then take their order and print their total do it in a while loop

guests = int(input("How many guests are there? "))
total = 0
while guests > 0:
    print(drinkMenu)
    drink = input("What drink would you like? ")
    if drink in drinkMenu:
        total += drinkMenu[drink]
    else:
        print("That drink is not on the menu.")
    guests -= 1
    
#take their order and print their total do it in a while loop

while True:
    print(menu)
    order = input("What would you like to order? ")
    if order in menu:
        total += menu[order]
    else:
        print("That item is not on the menu.")
    order_more = input("Would you like to order more? (yes/no) ")
    if order_more.lower() == 'no':
        break

print(f"Your total is ${total}")
