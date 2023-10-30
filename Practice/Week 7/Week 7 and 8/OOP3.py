class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def pricediff(self, yourcar):
        diff = self.price - yourcar.price
        return diff
    

mycar = Car("BMW", 1000000) 
yourcar = Car("Toyota", 500000)
p = mycar.pricediff(yourcar)
print(p)
