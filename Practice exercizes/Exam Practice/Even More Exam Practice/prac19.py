'''
3 criteria must be taken into account to identify leap years:

The year is evenly divisible by 4;

If the year can be evenly divided by 100, it is NOT a leap year, unless;

The year is also evenly divisible by 400. Then it is a leap year.

Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
'''

def leapYearFinder(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
        
print(leapYearFinder(2029))