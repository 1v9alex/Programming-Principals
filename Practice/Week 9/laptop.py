#make laptop class put name price rating then make a list of laptop, then displau the list of laptors from price low to high

class Laptop:
    def __init__(self,name,price,rating):
        self.name = name
        self.price = price
        self.rating = rating
        
        #now create laptop objects, put them in a list and zort them from price low to high
laptop1 = Laptop("Dell",1000,4.5)
laptop2 = Laptop("HP",800,3.5)
laptop3 = Laptop("Apple",2000,5)
laptop4 = Laptop("Lenovo",900,4)
laptop5 = Laptop("Acer",700,3)

laptoplist = [laptop1,laptop2,laptop3,laptop4,laptop5]

#sort the list based on the price
laptoplist.sort(key=lambda x: x.price)
for x in laptoplist:
    print(x.name,x.price,x.rating)
    
