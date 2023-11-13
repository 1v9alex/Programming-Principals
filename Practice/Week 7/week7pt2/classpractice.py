class Employee:
    def __init__(self,id,empname,empsalary,age):
        self.id = id
        self.empname = empname
        self.empsalary = empsalary
        self.age = age


    def showprofile(self):
        print(self.empname, self.empsalary)

    def incsalary(self,amount):
        self.empsalary = self.empsalary + amount
        
    def compare(self,emp):
        if self.empsalary > emp.empsalary:
            self.showprofile()
        else:
            emp.showprofile()
    #now making a function to copy an employee object
    def copy(self):
        return Employee(self.id,self.empname,self.empsalary,self.age)

Employee1 = Employee(1,"Alex",500000,17)
Employee2 = Employee(2, "not alex", 0,50)

Employee1.compare(Employee2)
Employee.compare(Employee1,Employee2)

Employee.copy(Employee1).showprofile()
'''#show will display an employees profile from the created object
def show(employee):
    return "ID: " + str(employee.id) + "\nName: " + employee.empname + "\nSalary: " + employee.empsalry + "\nAge: " + str(employee.age)

print(show(Employee1))
#line of 15 * to seperate the two
print("*"*15)
print(show(Employee2))

def increment(employee,amount):
    employee.empsalry = "$" + str(int(employee.empsalry[1:]) + amount)

increment(Employee2,10)

print(show(Employee2))'''