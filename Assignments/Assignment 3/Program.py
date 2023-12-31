from Bank import Bank

#Program class that handles the UI of the banking system
class Program:
    #Constructor intializes the program with a bank probject
    def __init__(self, bank):
        self.bank = bank
            
    #Method to display the main menu and handle user input
    def showMainMenu(self):
        while True:
            print("\n1. Open Account")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1" or choice == "Open Account":
                #Get account details from user
                accountType = input("Enter account type (savings/chequing): ")
                accountNumber = input("Enter account number: ")
                accountHolderName = input("Enter account holder's name: ")
                rateOfInterest = float(input("Enter rate of interest: "))
                currentBalance = float(input("Enter current balance: "))
                if accountType.lower() == "savings":
                    minimumBalance = float(input("Enter minimum balance: "))
                    additionalParam = minimumBalance
                elif accountType.lower() == "chequing":
                    overdraftAllowed = float(input("Enter overdraft limit: "))
                    additionalParam = overdraftAllowed
                else:
                    print("Invalid account type.")
                    return
                #Call the Bank's method to open the account
                try:
                    new_account = self.bank.openAccount(accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam)
                    print(f"Account {new_account.getAccountNumber()} opened successfully.")
                except ValueError as e:
                    print(f"Error opening account: {e}")
            elif choice == "2" or choice == "Select Account":
                accountNumber = input("Please enter the account number: ")
                account = self.bank.searchAccount(accountNumber)
                if account:
                    self.showAccountMenu(account)
                else:
                    print("Account not found.")
            elif choice == "3" or choice == "Exit":
                print("Thank you for using our banking system.")
                break
            else:
                print("Invalid choice. Please try again.")
                
    # Method to display the account menu for a specific account.
    def showAccountMenu(self, account):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Balance: {account.getCurrentBalance()}")
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print("Deposit successful.")
                except ValueError:
                    print("Invalid amount entered.")
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print("Withdrawal successful.")
                except ValueError:
                    print("Invalid amount entered.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    
    #method to start the program and show the main menu
    def run(self):
        self.showMainMenu()

#Entry point of the program
if __name__ == "__main__":
    bank = Bank("Bank")
    app = Program(bank)
    app.run()

