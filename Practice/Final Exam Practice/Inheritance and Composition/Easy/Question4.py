class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self,account_number,owner_name,balance,interest_rate):
        super().__init__(account_number,owner_name,balance)
        self.interest_rate = interest_rate
    
    
    def display_info(self):
        print(f"Hello {self.owner_name} here is your Account info: Account ID:{self.account_number}, Balance: ${self.balance} Interest Rate: {self.interest_rate}%")


class CheckingAccount(BankAccount):
    def __init__(self,account_number,owner_name,balance,transaction_limit):
        super().__init__(account_number,owner_name,balance)
        self.transaction_limit = transaction_limit
        
    def display_info(self):
        print(f"Hello {self.owner_name} here is your Account info: Account ID:{self.account_number}, Balance: ${self.balance} Transaction Limit: {self.transaction_limit}")

newSA = SavingsAccount(123456,"Alex",999999999,3.5)

newSA.display_info()

newCA = CheckingAccount(123,"Alex",999999999999,9999999999999)

newCA.display_info()