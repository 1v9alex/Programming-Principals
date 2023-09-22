#Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
#Write a program that displays the average speed in miles per hour. (Note that 1 mile is 1.6 kilometers.)

#Define the distance in kilometers
kilometers = 14

#Define the time in minutes
minutes = 45

#Define the time in seconds
seconds = 30


'''The formula to convert minutes to hours is as follows
 hours = minutes / 60
The formula to convert seconds to hours is as follows
 hours = seconds / 3600'''

#Calculate the time in hours
#We do not need to put brackets around the minutes and seconds as the division operator has a higher precedence than the addition operator as bedmas applies
hours = minutes / 60 + seconds / 3600

#Calculate the distance in miles
#1 mile is 1.6 kilometers and 1 kilometer is 0.621371 miles so we can convert Kilometers to miles in 2 different ways

#Method 1
miles = kilometers / 1.6

#Method 2
#miles = kilometers * 0.621371

#Calculate the average speed in MPH
avgspeed = miles / hours

#Round the average speed to 2 decimal places
avgspeed = round(avgspeed, 2)

#Display the averge speed in mph witho
print(f"The average speed is {avgspeed} miles per hour")