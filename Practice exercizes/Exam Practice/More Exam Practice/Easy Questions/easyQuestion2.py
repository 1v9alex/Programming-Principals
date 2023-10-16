"""
Strings & Conditional Statements: Ask the user for their name. If it's "Alice", print "Hello, Alice!", otherwise, print "Hello, stranger!"
"""

userName = input("Enter your name: ").lower()

if userName == "alice":
    print("Hello, Alice!")
else:
    print("Hello, Stranger!")