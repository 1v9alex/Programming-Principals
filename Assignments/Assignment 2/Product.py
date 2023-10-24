import random
class Product:
    def __init__(self,code,name,salePrice,manufactureCost,stockLevel,monthlyUnits):
        """
        Initializes the product class with the given parameters.
        
        Parameters:
        - code (int): The product code
        - name (str): The product name
        - salePrice (float): The product sale price
        - manufactureCost (float): The product manufacture cost for a single unit
        - stockLevel (int): The current stock level
        - monthlyUnits (int): The estimated monthly production
        """
        self.code = code
        self.name = name
        self.salePrice = salePrice
        self.manufactureCost = manufactureCost
        self.stockLevel = stockLevel
        self.monthlyUnits = monthlyUnits
    
    
    
    def monthlySimuation(self):
        """
        Simulates the monthly production and sales of the product
        Generates random units sold between monthlyUnits-10 and monthlyUnits+10 and adjusts the stock level accordingly.
        
        Returns:
        - unitsSold (int): The number of units sold
        """
        #Generate a random number of units sold within the range of monthlyUnits-10 and monthlyUnits+10
        unitsSold = random.randint(self.monthlyUnits-10, self.monthlyUnits+10)
        #Calculating the available stock after manufacturing for the month
        availableStock = self.stockLevel + self.monthlyUnits
        #Making sure the units sold does not exceed the available stock so there is no negative value for stock
        if unitsSold > availableStock:
            unitsSold = availableStock
        #Updating the stock by subtracting the units sold
        self.stockLevel = availableStock - unitsSold
        return unitsSold

    
    
    def netProfit(self,totalSoldUnits):
        """
        Calculated the net profit (or loss) for the year based on the total units sold
        Parameters:
        - totalSoldUnits (int): The total number of units sold for the year
        
        Returns:
        - netProfit (float): The net profit (or loss) for the year
        """
        #Calculate total revenue from sales
        totalRevenue = totalSoldUnits * self.salePrice
        #Calculate total manufacturing cost for the year
        totalManufacturingCost = self.monthlyUnits * 12 * self.manufactureCost
        #Return the difference as net profit (or loss)
        return totalRevenue - totalManufacturingCost
