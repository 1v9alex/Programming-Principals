"""
Selection, Iteration & Strings: Given a list of words, use a loop to print only those words that start with the letter 'a' or 'A'.
"""

wordList = ["alex","is","so","gangster","cool","and","amazing","Awesome"]
emptyList = []
for word in wordList:
    if "a" in word or "A" in word:
        emptyList.append(word)

print(emptyList)
print(wordList)