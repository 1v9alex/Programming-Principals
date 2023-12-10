'''
4. Values That Are Keys
We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. 
Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. Here is what we need to do:

Define the function to accept one parameter for our dictionary
Create an empty list to hold the values we find
Loop through every value in the dictionary
Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
After the loop, return the list of values which are also keys

Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
'''

# Write your values_that_are_keys function here:

def values_that_are_keys(my_dictionary):
    emptyList = []
    
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            emptyList.append(value)
    return emptyList
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]