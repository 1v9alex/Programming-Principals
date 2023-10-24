from Product import Product
class Application:
    def __init__(self):
        """
        Initializes the Application class with a product attribute set to None.
        """
        self.product = None

    def getValidInput(self, prompt, validationFN, errorMsg):
        """
        Gets input from the user and checks if its valid
        Parameters:
        - prompt (str): The prompt to display to the user when asking for input
        - validationFN (function): The function to use to validate the input
        - errorMsg (str): The error message to display if the input is invalid
        
        Returns:
        -value (str): The valid input from the user
        """
        while True:
            value = input(prompt)
            #Validate input using the validation function
            if validationFN(value):
                return value
            else:
                print(errorMsg)

    def createProduct(self):
        """
        Guides the user to input the product details and create a new product instance
        """
        #Getting the product attributes from the user then using validation function to ensure correct input format
        print("Welcome to the Programming Principles Sample Product Inventory")
        code = int(self.getValidInput("Please enter the product code: ", lambda x: x.isdigit() and 100 <= int(x) <= 1000, "Invalid product code."))
        name = self.getValidInput("Please enter the Product Name: ", lambda x: len(x) > 0, "Product name can't be empty.")
        stockLevel = int(self.getValidInput("Please enter the Current Stock: ", lambda x: x.isdigit() and int(x) > 0, "Invalid stock level."))
        salePrice = float(self.getValidInput("Please enter the Product Sale Price: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid sale price."))
        manufactureCost = float(self.getValidInput("Please enter the Product Manufacture Cost: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid manufacture cost."))
        monthlyUnits = int(self.getValidInput("Please enter the estimated monthly production: ", lambda x: x.isdigit() and int(x) >= 0, "Invalid monthly units."))
        
        #Creating a new product instance using the user provided information
        self.product = Product(code, name, salePrice, manufactureCost, stockLevel, monthlyUnits)

    def simulateAndReport(self):
        """
        Simulates sales and stock for 12 months and then displays a report
        """
        #Checks if a product has been created first
        if not self.product:
            print("Please create a product first!")
            return
        
        #Displaying the initial product information
        print("\n*******Programming Principles Sample Stock Statement*******\n")
        print(f"Product Code: {self.product.code}")
        print(f"Product Name: {self.product.name}\n")
        print(f"Sale Price: {self.product.salePrice} CAD")
        print(f"Manufacture Cost: {self.product.manufactureCost} CAD")
        print(f"Monthly Production: {self.product.monthlyUnits} units (Approx.)\n")

        totalSold = 0
        for month in range(1, 13): #Looping through 12 months
            unitsSold = self.product.monthlySimuation() #Simulating sales for the month
            totalSold += unitsSold
            #Displaying the data for each month
            print(f"Month {month}:")
            print(f"|        Manufactured: {self.product.monthlyUnits} units")
            print(f"|        Sold:        {unitsSold} units")
            print(f"|        Stock:       {self.product.stockLevel} units")
            
            if month == 12: #Adding an extra line after the 12th months data so it looks like the image in the assignment
                print("|")
        
        # Calculating the net amount
        netProfit = self.product.netProfit(totalSold)
        
        # Deciding how to present the result based on the calculated value
        if netProfit > 0:
            #If number is > 0 it will print the net profit
            print(f"Net Profit: ${netProfit:.2f} CAD")
        elif netProfit < 0:
            #If number is < 0 it will print the net loss
            print(f"Net Loss: ${abs(netProfit):.2f} CAD")
        else:
            #If the number is 0 it will print that you broke even
            print("You Broke Even!")


    def run(self):
        """
        Starts the application by creating a product and then simulating sales and displaying a report
        """
        self.createProduct() #Creating the product
        self.simulateAndReport() #Simulating sales and displaying a report

app = Application()
app.run()
