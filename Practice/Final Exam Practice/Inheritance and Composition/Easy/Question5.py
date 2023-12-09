class Shape:
    def area(self,a,b):
        print('area')
    
    def perimeter(self,a,b,c=0):
        pass


class Rectangle(Shape):
    def area(self,a,b):
        print(f"Area is {a*b}")
    
    def perimeter(self,a,b,c=0):
        print(f"Perimeter is {2*(a+b)}")

class Triangle(Shape):
    def area(self,a,b):
        print(f"Area is {(a*b)/(2)}")
    
    def perimeter(self,a,b,c=0):
        print(f"perimeter is {a+b+c}")


newR = Rectangle()

newR.area(4,3)

newR.perimeter(2,2)

newT = Triangle()

newT.area(2,2)

newT.perimeter(1,1,1)