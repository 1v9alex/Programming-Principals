class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price



class Electronics(Product):
    def __init__(self,product_id,name,price,warranty_period):
        super().__init__(product_id,name,price)
        self.warranty_period = warranty_period
    
    
    def displayInfo(self):
        print(f"{self.name} Product ID: {self.product_id}, Price: ${self.price}, Warranty Period {self.warranty_period} years")
        
        

newE = Electronics(134,"Laptop",500,3)

newE.displayInfo()