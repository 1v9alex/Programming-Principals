# get a number of students and their score and display the highest score
students = 0
score = 0
highestScore = 0
highestScoreName = ""


students = int(input("Enter the number of students: "))
for i in range (students):
    name = input("Enter the name of the student:")
    score = int(input("Enter the score of the student:"))
    if score > highestScore:
        highestScore = score
        highestScoreName = name
print("The highest score is", highestScore, "and the student is", highestScoreName)


'''
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the
total and average of the input values (not counting zeros). Your program
ends with the input 0. Display the average
'''


negCounter = 0
posCounter = 0
total = 0 

num = int(input("Enter a number: "))

while num != 0:
    if num > 0:
        posCounter += 1
        total += num
    else:
        negCounter += 1
        total += num
    num = int(input("Enter a number: "))
print("The number of positives is", posCounter)
print("The number of negatives is", negCounter)
print("The total is", total)
print("The average is", total/(posCounter+negCounter))