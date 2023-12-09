class Shape:
    def __init__(self,color):
        self.color = color
    
    def shapeColor(self):
        print("This shape has a color!")
    
    

class Circle(Shape):
    def shapeColor(self):
        print(f"This shape is the color {self.color}")

class Rectangle(Shape):
    def shapeColor(self):
        print(f"This shape is the color {self.color}")
        


newR = Rectangle("Purple")

newR.shapeColor()