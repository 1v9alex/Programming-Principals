"""
Strings, For Loops & Conditional Statements: Given a sentence, use a loop to count how many vowels it contains.
"""


vowels = "aeiou"

sentence = "alex is the best i love him so much oh my god you should inspect his amazing code haha wow"
sentence1 = "alex good"


vowelCount = 0

# without taking Y into account
for i in vowels:
    for word in sentence.lower():
        if i in word:
            vowelCount += 1

print(vowelCount)