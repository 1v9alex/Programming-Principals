'''
Write a program that displays the following table
 a      a^2      a^3
 1      1        1
 2      4        8
 3      9        27
 4      16       64
'''

#  Header
print("a      a^2      a^3")

# Loop through values 1 to 4
for a in range(1, 5):
    # Calculate a^2
    square = a ** 2
    #Calculate a^3
    cube = a ** 3
    # Display the row
    print(f"{a}      {square}      {cube}")