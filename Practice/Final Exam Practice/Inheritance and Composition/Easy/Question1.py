class Employee:
    def __init__(self,name,employee_id,department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
    
    def displayInfo(self):
        print(f"Name {self.name}, ID {self.employee_id} department {self.department}")

class Developer(Employee):
    def __init__(self,programming_languages):
        self.programming_languages = []
    
    def add_language(self,language):
        self.programming_languages.append(language)
        return self.programming_languages
    
    def displayList(self):
        print(f"Languages are {self.programming_languages}")

class Designer(Employee):
    def __init__(self,design_tools):
        self.design_tools = []
        
    def add_tool(self,tool):
        self.design_tools.append(tool)
        return self.design_tools
    
    def displayList(self):
        print(f"Tools used are {self.design_tools}")


newA = Employee("Alex",12,"Development")
newE = Developer(newA)

newE.add_language("Python")

newE.displayList()

newA.displayInfo()

newA2 = Employee("Alex",1,"Design")

newDS = Designer(newA2)

newDS.add_tool("Figma")

newDS.displayList()
        
        