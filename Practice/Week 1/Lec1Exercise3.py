#Write a program that displays the result of 1+2+3+4+5+6+7+8+9

#Method 1 Using a Loop the best way
#Initialize the sum
sum = 0
#Loop through the numbers 1 to 9
for sum in range(1, 10):
    #Add the number to the sum
    sum = sum + sum
#Display the result
print(f"The sum is {sum}")

#Method 2 Simple addition (very inefficient and not recommended)

#Calculate the result (this can be done in 1 line with the print statement)
result = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
#Display the result
print(f"The result is {result}")
