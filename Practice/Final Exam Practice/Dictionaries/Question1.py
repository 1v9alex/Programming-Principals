'''
1. Sum Values
For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up all of the values from the key-value pairs in the dictionary.

Here are the steps we need:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every value in the dictionary
Inside the loop, add each value to the sum
Return the sum

Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
'''

# Write your sum_values function here:
def sum_values(my_dictionary):
    counter = 0
    
    for value in my_dictionary.values():
        counter += value
    return counter

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6