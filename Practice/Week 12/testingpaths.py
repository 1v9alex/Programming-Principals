# Open the file
file = open("Practice/Week 12/testingpaths/text.txt", "r")

# Read the file line by line
for line in file:
    # Split the line into parts
    parts = line.split()

    # The name is the first part and the marks are the rest
    name = parts[0]
    marks = parts[1:]

    # Check if the student has 6 or more marks
    if len(marks) >= 6:
        print(f"Student {name} has 6 or more marks")

# Close the file
file.close()