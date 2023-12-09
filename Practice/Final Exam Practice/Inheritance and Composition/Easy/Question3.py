class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def displayInfo(self):
        print(f"student name is {self.name} their age is {self.age}")


class Student(Person):
    def __init__(self,name,age,enrolled_courses=None):
        super().__init__(name,age)
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []
    
    def addCourse(self,course):
        self.enrolled_courses.append(course)
        return self.enrolled_courses
    
    def displayCourse(self):
        print(f"{self.name} is enrolled in {self.enrolled_courses}")


class Teacher(Person):
    def __init__(self,name,age,courses_taught = None):
        super().__init__(name,age)
        self.courses_taught = courses_taught if courses_taught is not None else []
    
    def addCourseTaught(self,course):
        self.courses_taught.append(course)
        return self.courses_taught
    
    def displayCoursesTaught(self):
        courses = ",".join(self.courses_taught)
        print(f"{self.name} Teaches {courses}")


newP = Person("Alex",18)

newS = Student("Alex",18)

newS.addCourse("Programming")

newS.displayCourse()

newP.displayInfo()

newT = Teacher("Alex",70)

newT.addCourseTaught("Math")
newT.addCourseTaught("English")

newT.displayCoursesTaught()