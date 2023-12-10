'''
3. Add Ten
Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return the modified dictionary. 

Here is what we need to do:

Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary

Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary
'''

# Write your add_ten function here:
def add_ten(my_dictionary):
    for key,value in my_dictionary.items():
        my_dictionary[key] = value+10
    return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}