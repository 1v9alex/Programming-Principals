def calculate_and_print_averages(filename):
    with open(filename, "r") as file:
        for line in file:
            # Split the line into parts
            parts = line.split()

            # The name is the first part and the marks are the rest
            name = parts[0]
            marks = parts[1:]

            # Convert marks from string to integers
            scores = [int(mark) for mark in marks]

            # Calculate the average score
            avgScore = sum(scores) / len(scores)

            # Print the average score rounded to two decimal places
            print(f"{name.capitalize()}'s average grade: {round(avgScore, 2)}")

# Call the function with the path to  file
calculate_and_print_averages("Final Exam Question/studentdata.txt")
