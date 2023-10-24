numStudents = 0
highScore = 0
studentScore = 0
numStudents = int(input("Enter number of students: "))
studentName = ""
highScoreName = ""
for i in range(numStudents):
    studentName = input("Enter the students name ")
    studentScore = int(input("Enter the students score "))
    if studentScore > highScore:
        highScore = studentScore
        highScoreName = studentName
print(f"{highScoreName} had the highest score with a whopping {highScore}")
        