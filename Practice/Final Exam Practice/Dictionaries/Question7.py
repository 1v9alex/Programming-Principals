'''
2. Frequency Count
This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. 
This function will also accept a list of strings as input and return a new dictionary. Here is what we need to do:

Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, if the string is NOT already in our dictionary, store the string as a key with a value of 0 in our dictionary. Otherwise, if the string is already in our dictionary, 
increment the value by 1.
After the loop, return the new dictionary

Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
The function should return a dictionary containing the frequency of each element in words.
'''

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    word_frequency = {}
    counter = 0
    
    for word in words:
        if word not in word_frequency.keys():
            word_frequency[word] =1
        elif word in word_frequency.keys():
            word_frequency[word] += 1
    return word_frequency
        
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}