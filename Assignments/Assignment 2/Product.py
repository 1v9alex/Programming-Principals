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
        unitsSold = random.randint(self.monthlyUnits-10, self.monthlyUnits+10)
        # Check if unitsSold exceeds available stock
        available_stock = self.stockLevel + self.monthlyUnits
        if unitsSold > available_stock:
            unitsSold = available_stock
        # Update the stock level
        self.stockLevel = available_stock - unitsSold
        return unitsSold

    
    
    def netProfit(self,totalSoldUnits):
        totalRevenue = totalSoldUnits * self.salePrice
        totalManufacturingCost = self.monthlyUnits * 12 * self.manufactureCost
        return totalRevenue - totalManufacturingCost
