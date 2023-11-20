from Bank import Bank

class Program:
    def __init__(self,bank):
        self.bank = bank
    
    def showMainMenu(self):
        while True:
            print("\n1. Open Account")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1" or choice == "Open Account":
                self.openAccount()
            elif choice == "2" or choice == "Select Account":
                self.selectAccount()
            elif choice == "3" or choice == "Exit":
                print("Thank you for using our banking system.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def showAccountMenu(self,account):
        #TODO: Implement this method
        pass
    
    def run(self):
        #TODO implement this method
        pass
    
    