class Calculator:
    def calculate(self,a,b):
        pass

class addCalculator(Calculator):
    def calculate(self,a,b):
        print(a+b)

class subtractCalculator(Calculator):
    def calculate(self,a,b):
        print(a-b)


newC = addCalculator()

newC.calculate(1,2)

newS = subtractCalculator()

newS.calculate(2,1)