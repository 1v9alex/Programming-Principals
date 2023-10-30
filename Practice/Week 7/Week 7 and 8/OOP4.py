class Account:
    def __init__(self,id,accname,balance=1000):
        self.id=id
        self.accname=accname
        self.balance=balance
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")
    def deposit(self,amount):
        self.balance += amount
        print("Deposit successful")
    def getBalance(self):
        return self.balance

acc1 = Account(1,"John",1000)
acc2 = Account(2,"Jane",1000)

acc1.withdraw(500)
acc2.deposit(500)
print(acc1.getBalance())
print(acc2.getBalance())
acc1.withdraw(5000)
acc2.withdraw(500)
print(acc1.getBalance())
print(acc2.getBalance())
acc1.deposit(500)
acc2.deposit(500)
print(acc1.getBalance())
print(acc2.getBalance())
