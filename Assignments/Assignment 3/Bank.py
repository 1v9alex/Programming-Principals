from Account import Account, SavingsAccount, ChequingAccount
class Bank:
    #Constructor intializes the bank name and accounts list
    def __init__(self,bankName):
        #Setting the bank name
        self._bankName = bankName # private variable to store the bank name
        self._accounts = [] # private variable to store the accounts
        #Creating 5 hardcoded accounts and appending them to the accounts list
        self._accounts.append(SavingsAccount("12345", "John Doe", 0.02, 10000.0, 500.0))
        self._accounts.append(SavingsAccount("12346", "Jane Smith", 0.03, 15000.0, 1000.0))
        self._accounts.append(ChequingAccount("12347", "Alice Brown", 0.01, 5000.0, 1000.0))
        self._accounts.append(ChequingAccount("12348", "Bob Martin", 0.01, 3000.0, 500.0))
        self._accounts.append(SavingsAccount("12349", "Charlie Johnson", 0.04, 20000.0, 2000.0))
    
    
    

    #Method to create a new account of a specified type and add it to the accounts list.
    def openAccount(self, accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam):
        if accountType.lower() == "savings":
            #For SavingsAccount, additionalParam is assumed to be minimum balance
            account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam)
        elif accountType.lower() == "chequing":
            #For ChequingAccount, additionalParam is assumed to be overdraft limit
            account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam)
        else:
            raise ValueError("Invalid account type.")
        self._accounts.append(account)
        return account
    
    #Method to search for an account by account number and return it if found.
    def searchAccount(self,accountNumber):
        for account in self._accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        return None