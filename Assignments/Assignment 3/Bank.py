from Account import SavingsAccount, ChequingAccount
class Bank:
    def __init__(self,bankName):
        self._bankName = bankName
        self._accounts = []
    
    def openAccount(self,accountType,*args):
        if accountType == "Savings":
            account = SavingsAccount(*args)
        elif accountType == "Chequing":
            account = ChequingAccount(*args)
        else:
            raise ValueError("Invalid account type.")
        self._accounts.append(account)
        return account
    
    def searchAccount(self,accountNumber):
        for account in self._accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        return None