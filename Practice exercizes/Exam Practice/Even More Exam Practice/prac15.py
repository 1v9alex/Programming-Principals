"""
Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

Mark

Grade

>= 90

A

[80-90)

B

[70-80)

C

[60-70)

D

< 60

F

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

Test your function by printing the mark and the grade for a number of different marks.
"""

def markCalculator(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80 and mark <= 90:
        return "B"
    elif mark >= 70 and mark <= 80:
        return "C"
    elif mark >= 60 and mark <= 70:
        return "D"
    else:
        return "F"
    

print(markCalculator(79.99999))