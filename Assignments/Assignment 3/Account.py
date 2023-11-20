class Account:
    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
        
    def getAccountNumber(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def getCurrentBalance(self):
        return self._currentBalance
    
    def deposit(self,amount):
        if amount > 0:
            self._currentBalance += amount
        else:
            raise ValueError("Deposit amount must be greater than 0.")
    
    def withdraw(self,amount):
        if amount > 0:
            self._currentBalance -= amount
        else:
            raise ValueError("Withdraw amount must be greater than 0.")
    
class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance
    
    def withdraw(self, amount):
        if self._currentBalance - amount >= self._minimumBalance:
            super().withdraw(amount)
        else:
            raise ValueError("Withdrawal would bring balance below minimum.")
    
class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftAllowed = overdraftAllowed
    
    def withdraw(self, amount):
        if self._currentBalance + self._overdraftAllowed >= amount:
            super().withdraw(amount)
        else:
            raise ValueError("Overdraft limit reached")