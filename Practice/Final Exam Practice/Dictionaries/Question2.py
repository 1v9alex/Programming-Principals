'''
2. Even Keys
Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even key within the dictionary. 

Here are the steps:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum

Create a function called sum_even_keys that takes a dictionary named my_dictionary, 
with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
'''

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    counter = 0
    for key,value in my_dictionary.items():
        if key % 2 == 0:
            counter +=value
    return counter
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6