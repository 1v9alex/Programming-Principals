class Vehicle:
    def __init__(self,number_of_wheels):
        self.number_of_wheels = number_of_wheels
        
    def display_info(self):
        print(f"This vehicle has {self.number_of_wheels} wheels.")
    
    
class Car(Vehicle):
    def __init__(self):
        super().__init__(number_of_wheels=100)


my_car = Car()
my_car.display_info()
            
        