
class Laptop:
    def __init__(self,model,price,rating,brand):
        self.model = model
        self.price = price
        self.rating = rating
        self.brand = brand
        
    #Getter and setter methods for model
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
    
    #getter and setter for price
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
    
    
    #getter and setter for rating
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        self.__rating = rating
    
    #getter and setter for brand
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
    
    def __str__(self):
        return "Model: " + self.model + " Price: " + str(self.price) + " Rating: " + str(self.rating)
    
    
laptops = {
    "Laptop1": Laptop("Macbook Pro", 1000, 4.5, "Apple"),
    "Laptop2": Laptop("Macbook Air", 800, 4.0, "Apple"),
    "Laptop3": Laptop("HP Omen", 700, 3.5, "HP"),
    "Laptop4": Laptop("HP Pavilion", 600, 3.0, "HP"),
    "Laptop5": Laptop("Dell XPS", 900, 4.0, "Dell"),
    "Laptop6": Laptop("Dell Inspiron", 500, 3.5, "Dell"),
    "Laptop7": Laptop("Asus Zenbook", 800, 4.0, "Asus"),
    "Laptop8": Laptop("Asus Vivobook", 600, 3.5, "Asus"),
    "Laptop9": Laptop("Lenovo Thinkpad", 700, 4.0, "Lenovo"),
    "Laptop10": Laptop("Lenovo Ideapad", 500, 3.5, "Lenovo"),
    "Laptop11": Laptop("Acer Swift", 600, 4.0, "Acer"),
    "Laptop12": Laptop("Acer Aspire", 400, 3.5, "Acer"),
    "Laptop13": Laptop("Microsoft Surface", 900, 4.0, "Microsoft"),
    "Laptop14": Laptop("Microsoft Surface Pro", 800, 4.5, "Microsoft"),
    "Laptop15": Laptop("Samsung Notebook", 700, 3.5, "Samsung"),
    "Laptop16": Laptop("Samsung Galaxybook", 600, 3.0, "Samsung"),
    "Laptop17": Laptop("Razer Blade", 1000, 4.0, "Razer"),
    "Laptop18": Laptop("Razer Blade Stealth", 800, 4.5, "Razer"),
    "Laptop19": Laptop("MSI Stealth", 900, 4.0, "MSI"),
    "Laptop20": Laptop("MSI Prestige", 700, 3.5, "MSI"),
    "Laptop21": Laptop("Google Pixelbook", 800, 4.0, "Google"),
    "Laptop22": Laptop("Google Pixelbook Go", 600, 3.5, "Google"),
    "Laptop23": Laptop("Huawei Matebook", 700, 4.0, "Huawei"),
    "Laptop24": Laptop("Huawei Matebook X", 500, 3.5, "Huawei"),
    "Laptop25": Laptop("LG Gram", 600, 4.0, "LG"),
    "Laptop26": Laptop("LG Gram 2-in-1", 500, 3.5, "LG"),
    "Laptop27": Laptop("Toshiba Portege", 600, 4.0, "Toshiba"),
    "Laptop28": Laptop("Toshiba Tecra", 500, 3.5, "Toshiba"),
    "Laptop29": Laptop("Xiaomi Mi Notebook", 700, 4.0, "Xiaomi"),
    "Laptop30": Laptop("Xiaomi Mi Notebook Pro", 500, 3.5, "Xiaomi")
}

#method for searching my model or brand i.e apple or macbook  
def searchByModel(query):
    return [laptop for laptop in laptops.values() if laptop.model == query or laptop.brand == query]

#method to search by max price
def searchByMaxPrice(maxPrice):
    return [laptop for laptop in laptops.values() if laptop.price <= maxPrice]

#Menu for user to interact with
while True:
    #printing the options for the user
    print("1. Search by model or brand")
    print("2. Search by maximum price")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    #getting the users choice
    if choice == "1":
        query = input("Enter model or brand: ")
        results = searchByModel(query)
        #if no results that match the filters are found
        if not results:
            print("No laptops found that match your criteria.")
            continue_shopping = input("Would you like to continue shopping? (y/n): ")
            if continue_shopping.lower() == 'n':
                break
            else:
                continue
            #printing the results
        for i, laptop in enumerate(results):
            print(f"{i+1}. {laptop.model} ({laptop.brand})")
            
            #starting a loop to get the users choice on if they want to see more info on a laptop
        while True:
            laptop_choice = input("Enter the number of a laptop to view more information, or 'b' to go back: ")
            if laptop_choice.lower() == 'b':
                break
            elif laptop_choice.isdigit() and 1 <= int(laptop_choice) <= len(results):
                print(results[int(laptop_choice)-1])
            else:
                print("Invalid choice. Please try again.")
                #if the user wants to search by max price
    elif choice == "2":
        max_price = float(input("Enter maximum price: "))
        results = searchByMaxPrice(max_price)
        if not results:
            print("No laptops found that match your .")
            continue_shopping = input("Would you like to continue shopping? (y/n): ")
            if continue_shopping.lower() == 'n':
                break
            else:
                continue
            #printing the results
        for i, laptop in enumerate(results):
            print(f"{i+1}. {laptop.model} ({laptop.brand})")
            
            #starting a loop to get the users choice on if they want to see more info on a laptop
        while True:
            laptop_choice = input("Enter the number of a laptop to view more information, or 'b' to go back: ")
            if laptop_choice.lower() == 'b':
                break
            elif laptop_choice.isdigit() and 1 <= int(laptop_choice) <= len(results):
                print(results[int(laptop_choice)-1])
            else:
                print("Invalid choice. Please try again.")
    elif choice == "3":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice, please try again")

