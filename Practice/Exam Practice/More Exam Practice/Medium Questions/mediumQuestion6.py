"""
Strings & Conditional Statements: Check if a user-provided string is a palindrome.
"""

userString = input("Enter a string: ")
palindrome = ""
for i in range(len(userString)-1,-1,-1):
    palindrome += userString[i]
    if userString == palindrome:
        print("it is a palindrome")
    else:
        print("not")