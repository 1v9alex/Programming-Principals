"""
Strings, Loops & Selection: Given a list of words, find the word with the most vowels.
"""

vowels = "aeiou"

wordList = ["alexander", "inooooos"]

vowelCount = 0
mostVowels = ""


for word in wordList:
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
            
    if count > vowelCount:
        vowelCount = count
        mostVowels = word



                
print(mostVowels)


