'''
4. Count First Letter
This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. 
We need to calculate the number of people who have the same first letter in their last name. Here are the steps we need:

Define the function to accept one parameter for our dictionary
Create a new empty dictionary called letters
Loop through every key in our names dictionary
Inside the loop, get the first letter of the last name we are looking at. If the first letter is not in our letter dictionary, 
add it as a key and set the value to the number of people that have that last name. Otherwise, if the first letter is already in our letter dictionary, 
increment the value stored with that key by the number of people that have that last name
After the loop, return the letters dictionary

Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

{"S" : 4, "L": 3}

'''

# Write your count_first_letter function here:
def count_first_letter(names):
    letters = {}
    
    for key in names.keys():
        if key[0] not in letters.keys():
            letters[key[0]] = len(names[key])
        elif key[0] in letters.keys():
            letters[key[0]] += len(names[key])

    return letters


        
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}