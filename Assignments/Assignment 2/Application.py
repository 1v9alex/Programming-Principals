from Product import Product
class Application:
    def __init__(self):
        self.product = None

    def get_valid_input(self, prompt, validation_fn, error_msg):
        while True:
            value = input(prompt)
            if validation_fn(value):
                return value
            else:
                print(error_msg)

    def create_product(self):
        code = int(self.get_valid_input("Enter Product Code (100-1000): ", lambda x: x.isdigit() and 100 <= int(x) <= 1000, "Invalid product code."))
        name = self.get_valid_input("Enter Product Name: ", lambda x: len(x) > 0, "Product name can't be empty.")
        salePrice = float(self.get_valid_input("Enter Product Sale Price: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid sale price."))
        manufactureCost = float(self.get_valid_input("Enter Product Manufacture Cost: ", lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0, "Invalid manufacture cost."))
        stockLevel = int(self.get_valid_input("Enter Stock Level: ", lambda x: x.isdigit() and int(x) > 0, "Invalid stock level."))
        monthlyUnits = int(self.get_valid_input("Enter Estimated Monthly Units Manufactured: ", lambda x: x.isdigit() and int(x) >= 0, "Invalid monthly units."))

        self.product = Product(code,name,salePrice,manufactureCost,stockLevel,monthlyUnits)

    def simulate_and_report(self):
        if not self.product:
            print("Please create a product first!")
            return

        total_sold = 0
        for month in range(1, 13):
            units_sold = self.product.monthlySimuation()
            total_sold += units_sold
            print(f"Month {month}:")
            print(f"Units Sold: {units_sold}")
            print(f"Stock Level: {self.product.stockLevel}")
            print()

        net_profit = self.product.netProfit(total_sold)
        print(f"Net Profit/Loss over 12 months: ${net_profit:.2f}")

    def run(self):
        self.create_product()
        self.simulate_and_report()

app = Application()
app.run()
