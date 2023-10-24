import random
class Product:
    def __init__(self,code,name,salePrice,manufactureCost,stockLevel,monthlyUnits):
        self.code = code
        self.name = name
        self.salePrice = salePrice
        self.manufactureCost = manufactureCost
        self.stockLevel = stockLevel
        self.monthlyUnits = monthlyUnits
    
    
    
    def monthlySimuation(self):
        unitsSold = random.randint(self.monthlyUnits-10,self.monthlyUnits+10)
        #generating a predicted stock statement for 12 months
        self.stockLevel = self.stockLevel + self.monthlyUnits - unitsSold
        return unitsSold
    
    
    def netProfit(self,totalSoldUnits):
        return (totalSoldUnits * self.salePrice) - (self.monthlyUnits * self.manufactureCost)