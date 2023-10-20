'''
It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) 
and you return home after 10 nights you would return home on a Saturday (day 6)
Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
'''

startingDate = int(input("Enter the starting day of your vacation (0-6): "))
stayLength = int(input("How many days will you stay?: "))


vacationLength = startingDate + stayLength

backHomeDay = vacationLength % 6

print(backHomeDay)

