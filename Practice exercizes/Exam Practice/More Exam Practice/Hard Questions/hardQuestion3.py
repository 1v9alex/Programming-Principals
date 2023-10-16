"""
Functions, Strings & Algorithms: Write a function that takes in a string and returns the string with its words reversed (e.g., "Hello World" -> "World Hello").
"""


def reversedString(reversed):
    words = reversed.split()
    reversedWords = words[::-1]
    reversedString = ' '.join(reversedWords)
    return reversedString


print(reversedString("Hello World"))
print(reversedString("Alex Is Awesome"))