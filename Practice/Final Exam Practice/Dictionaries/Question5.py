'''
5. Largest Value
For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. 
This is a twist on the max algorithm since it is using a dictionary rather than a list. These are the steps:

Define the function to accept one parameter for our dictionary
Initialize the starting key to a very low number
Initialize the starting value to a very low number
Iterate through the dictionary’s key/value pairs.
Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
Once you are done iterating through all key/value pairs, return the key which has the largest value

Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
'''
# Write your max_key function here:
'''def max_key(my_dictionary):
    largest = 0
    largestKey = 0
    for key in my_dictionary.keys():
        a = my_dictionary[key]
        if a > largest:
            largest = a
            largestKey = key
    return largestKey
        
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"'''


#method 2 (the better way of doing it)
def max_key(my_dictionary):
    largest = 0
    largestKey = ""
    
    for key,value in my_dictionary.items():
        if value > largest:
            largest = value
            largestKey = key
    return largestKey

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"