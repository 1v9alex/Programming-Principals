f = open("Practice\Final Exam Practice\Files\Practice 1\data.txt", "r")

for line in f:
    # Split the line into parts
    parts = line.split()

    # The name is the first part and the marks are the rest
    name = parts[0]
    marks = parts[1:]

    # Check if the student has 6 or more marks
    scores = [int(mark) for mark in marks]
    
    avgScore = sum(scores) / len(scores)
    
    
    print(round(avgScore,2))
f.close()