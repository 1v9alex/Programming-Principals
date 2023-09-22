'''Write a program that displays the area and perimeter of a circle that has a radius of 5.5 using the following formulas
 area = radius * radius * pi
 perimeter = 2 * radius * pi
 pi can be computed using the following formula
 pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)'''

#Define the radius
radius = 5.5
#Calculate pi
pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
#Calculate the area
area = radius * radius * pi
#Calculate the perimeter
perimeter = 2 * radius * pi

#Display the results this answer will not be rounded (this can be done in 1 line with the print statement but i am using 2 lines for clarity)
print(f"The area is {area}")
print(f"The perimeter is {perimeter}")
#Display the results this answer will be rounded to 1 decimal place as thats what the question uses
print(f"The area is {round(area, 1)}")
print(f"The perimeter is {round(perimeter, 1)}")