'''
3. Unique Values
Now let’s try reading a dictionary as input and finding how many values are unique. 
The function should return a number which is the count of all values from the dictionary without including duplicates. 

These are the steps:

Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list

Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.
'''

# Write your unique_values function here:
def unique_values(my_dictionary):
    
    emptyList = []
    
    for value in my_dictionary.values():
        if value not in emptyList:
            emptyList.append(value)
    return len(emptyList)
        
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1