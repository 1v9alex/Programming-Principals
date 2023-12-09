class Animal:
    def speak(self):
        print("I am an animal")



class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")
        



newD = Dog()

newD.speak()