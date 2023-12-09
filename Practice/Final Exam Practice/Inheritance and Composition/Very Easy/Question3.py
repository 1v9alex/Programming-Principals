class Animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        print("This animal makes a sound.")
        

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} barks!")


class Bird(Animal):
    def sound(self):
        print(f"{self.name} chirps!")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows!")


c = Cat("wiskers")

c.sound()