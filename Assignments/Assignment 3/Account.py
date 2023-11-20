class Account:
    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
        
    def getAccountNumber(self):
        #TODO: Implement this method
        pass
    
    def getAccountHolderName(self):
        #TODO: Implement this method
        pass
    
    def getRateOfInterest(self):
        #TODO: Implement this method
        pass
    
    def getCurrentBalance(self):
        #TODO: Implement this method
        pass
    
    def deposit(self,amount):
        #TODO Implement this method
        pass
    
    def withdraw(self,amount):
        #TODO Implement this method
        pass
    
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder_name, rate_of_interest, current_balance, minimum_balance):
        super().__init__(account_number, account_holder_name, rate_of_interest, current_balance)
        self._minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        #TODO Implement this method
        pass
    
class ChequingAccount(Account):
    def __init__(self, account_number, account_holder_name, rate_of_interest, current_balance, overdraft_allowed):
        super().__init__(account_number, account_holder_name, rate_of_interest, current_balance)
        self._overdraft_allowed = overdraft_allowed
    
    def withdraw(self, amount):
        #TODO Implement this method
        pass

        
        
