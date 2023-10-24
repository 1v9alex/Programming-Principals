"""
Strings, Conditional Statements & Algorithms: Determine if a user-provided string has balanced parentheses.
"""

userString = input("Enter a string: ")


stack = []

balanced = True

for char in userString:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if not stack:
            balanced = False
            break
        stack.pop()

if balanced and len(stack) == 0:
    print("The string has balanced parentheses")
else:
    print("The string does not have balanced parentheses")
    