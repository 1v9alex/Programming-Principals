from Account import Account, SavingsAccount, ChequingAccount
class Bank:
    def __init__(self,bankName):
        self._bankName = bankName
        self._accounts = []
    
    def openAccount(self, accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam):
        if accountType.lower() == "savings":
            # For SavingsAccount, additionalParam is assumed to be minimum balance
            account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam)
        elif accountType.lower() == "chequing":
            # For ChequingAccount, additionalParam is assumed to be overdraft limit
            account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, additionalParam)
        else:
            raise ValueError("Invalid account type.")
        self._accounts.append(account)
        return account
    
    def searchAccount(self,accountNumber):
        for account in self._accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        return None