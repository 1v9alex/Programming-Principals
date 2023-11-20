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
                bank.openAccount()
            elif choice == "2" or choice == "Select Account":
                self.selectAccount()
            elif choice == "3" or choice == "Exit":
                print("Thank you for using our banking system.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def showAccountMenu(self,account):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")
            if choice == "1" or choice == "Check Balance":
                print(f"Balance: {account.getCurrentBalance()}")
            elif choice == "2" or choice == "Deposit":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful.")
            elif choice == "3" or choice == "Withdraw":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                print("Withdrawal successful.")
            elif choice == "4" or choice == "Exit Account":
                print("Exiting account.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def run(self):
        self.showMainMenu()
    
    def openAccount(self):
        # Collect required information to open an account
        account_type = input("Enter account type (Savings/Chequing): ")
        account_number = input("Enter account number: ")
        account_holder_name = input("Enter account holder's name: ")
        rate_of_interest = float(input("Enter rate of interest: "))
        current_balance = float(input("Enter current balance: "))

        if account_type == "Savings":
            minimum_balance = float(input("Enter minimum balance: "))
            self.bank.openAccount(account_type, account_number, account_holder_name, rate_of_interest, current_balance, minimum_balance)
        elif account_type == "Chequing":
            overdraft_allowed = float(input("Enter overdraft amount allowed: "))
            self.bank.openAccount(account_type, account_number, account_holder_name, rate_of_interest, current_balance, overdraft_allowed)
        else:
            print("Invalid account type provided.")



if __name__ == "__main__":
    # Example initialization
    bank = Bank("ExampleBank")
    app = Program(bank)
    app.run()