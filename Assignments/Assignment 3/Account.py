class Account:
    # Constructor intializes the account number, account holder name, rate of interest and current balance
    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
    
    #Getter methods to return the account number, account holder name, rate of interest and current balance
    def getAccountNumber(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def getCurrentBalance(self):
        return self._currentBalance
    
    #Setter methods to set the account number, account holder name, rate of interest and current balance
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

#SavingsAccount inherits from Account
class SavingsAccount(Account):
    #Constructor intializes the account number, account holder name, rate of interest, current balance and minimum balance
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        #Call the parent class's constructor
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance
    #Overridden withdraw method to check for minimum balance requirement.
    def withdraw(self, amount):
        if self._currentBalance - amount >= self._minimumBalance:
            super().withdraw(amount)
        else:
            raise ValueError("Withdrawal would bring balance below minimum.")
        
#ChequingAccount inherits from Account
class ChequingAccount(Account):
    #Constructor intializes the account number, account holder name, rate of interest, current balance and overdraft limit
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftAllowed):
        #Call the parent class's constructor
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftAllowed = overdraftAllowed
    #Overridden withdraw method to check for overdraft limit.
    def withdraw(self, amount):
        if self._currentBalance + self._overdraftAllowed >= amount:
            super().withdraw(amount)
        else:
            raise ValueError("Overdraft limit reached")