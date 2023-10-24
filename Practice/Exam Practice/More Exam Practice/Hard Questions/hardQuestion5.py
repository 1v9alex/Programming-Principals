"""
Functions, Algorithms & Strings: Write a function that counts how many times a particular letter appears in a given string.
"""


def letterCounter(string,letter):
    counter = 0
    for letters in string.lower():
        if letter in letters:
            counter += 1
    return counter


print(letterCounter("alex is amazing","h"))