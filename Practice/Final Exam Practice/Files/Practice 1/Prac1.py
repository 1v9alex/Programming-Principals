f = open("Practice\Final Exam Practice\Files\Practice 1\data.txt", "r")

for line in f:
    values = line.split()
    print(values[0])
f.close()