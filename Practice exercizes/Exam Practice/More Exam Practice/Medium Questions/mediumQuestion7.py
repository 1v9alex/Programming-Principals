"""
Data Types & Selection: Create a dictionary of three user-provided keys and values, then print the value for a user-asked key.
"""

data_dict = {}

for _ in range(3):
    key = input("Enter a key: ")
    value = input(f"Enter a value for {key}: ")
    data_dict[key] = value

search_key = input("Which key's value would you like to retrieve? ")

if search_key in data_dict:
    print(f"The value for key '{search_key}' is: {data_dict[search_key]}")
else:
    print(f"No value found for key '{search_key}'")