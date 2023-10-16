"""
For Loops & Strings: Given a string, use a for loop to print its characters in reverse order.
"""

testString = "1v9Alex"
reversedString = ""

for char in range(len(testString)-1,-1,-1):
    reversedString += testString[char]

print(reversedString)
#1v9Alex
#xela9v1