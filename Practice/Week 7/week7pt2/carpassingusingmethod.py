class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    #func to print a fraction in format a/b
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def add(self,fraction):
        return Fraction((self.numerator * fraction.denominator) + (fraction.numerator * self.denominator), self.denominator * fraction.denominator)
    
    def subtract(self,fraction):
        return Fraction((self.numerator * fraction.denominator) - (fraction.numerator * self.denominator), self.denominator * fraction.denominator)
    
    def multiply(self,fraction):
        return Fraction(self.numerator * fraction.numerator, self.denominator * fraction.denominator)

print(Fraction(1,2).add(Fraction(1,2)))

print(Fraction(6,9))

print(Fraction.multiply(Fraction(5,7),Fraction(6,8)))