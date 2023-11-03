class Employee:
    def __init__(self,id,empname,empsalary,age):
        self.id = id
        self.empname = empname
        self.empsalry = empsalary
        self.age = age


Employee1 = Employee(1,"Alex","$500000",17)
Employee2 = Employee(2, "not alex", "$0",50)

#show will display an employees profile from the created object
def show(employee):
    return "ID: " + str(employee.id) + "\nName: " + employee.empname + "\nSalary: " + employee.empsalry + "\nAge: " + str(employee.age)

print(show(Employee1))
#line of 15 * to seperate the two
print("*"*15)
print(show(Employee2))

def increment(employee,amount):
    employee.empsalry = "$" + str(int(employee.empsalry[1:]) + amount)

increment(Employee2,10)

print(show(Employee2))