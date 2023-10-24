from Product import Product
class Application:
    def __init__(self):
        self.product = None

    def getValidInput(self, prompt, validationFN, error_msg):
        while True:
            value = input(prompt)
            if validationFN(value):
                return value
            else:
                print(error_msg)

    def createProduct(self):
        print("Welcome to the Programming Principles Sample Product Inventory")
        code = int(self.getValidInput("Please enter the product code: ", lambda x: x.isdigit() and 100 <= int(x) <= 1000, "Invalid product code."))
        name = self.getValidInput("Please enter the Product Name: ", lambda x: len(x) > 0, "Product name can't be empty.")
        stockLevel = int(self.getValidInput("Please enter the Current Stock: ", lambda x: x.isdigit() and int(x) > 0, "Invalid stock level."))
        salePrice = float(self.getValidInput("Please enter the Product Sale Price: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid sale price."))
        manufactureCost = float(self.getValidInput("Please enter the Product Manufacture Cost: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid manufacture cost."))
        monthlyUnits = int(self.getValidInput("Please enter the estimated monthly production: ", lambda x: x.isdigit() and int(x) >= 0, "Invalid monthly units."))

        self.product = Product(code, name, salePrice, manufactureCost, stockLevel, monthlyUnits)

    def simulateAndReport(self):
        if not self.product:
            print("Please create a product first!")
            return

        print("\n*******Programming Principles Sample Stock Statement*******\n")
        print(f"Product Code: {self.product.code}")
        print(f"Product Name: {self.product.name}\n")
        print(f"Sale Price: {self.product.salePrice} CAD")
        print(f"Manufacture Cost: {self.product.manufactureCost} CAD")
        print(f"Monthly Production: {self.product.monthlyUnits} units (Approx.)\n")

        totalSold = 0
        for month in range(1, 13):
            unitsSold = self.product.monthlySimuation()
            totalSold += unitsSold
            print(f"Month {month}:")
            print(f"|        Manufactured: {self.product.monthlyUnits} units")
            print(f"|        Sold:        {unitsSold} units")
            print(f"|        Stock:       {self.product.stockLevel} units\n")

        netProfit = self.product.netProfit(totalSold)
        print(f"Net Profit: ${netProfit:.2f} CAD")

    def run(self):
        self.createProduct()
        self.simulateAndReport()

app = Application()
app.run()
