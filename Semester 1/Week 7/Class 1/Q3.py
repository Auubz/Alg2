class BankAccount():

    def __init__(self,balance):
        self.balance == balance


    def withdraw (self, amount):
        print(int(balance) - amount)

    def deposit (self, amount2):
        print(int(balance + amount2))


b = BankAccount(10)
b.deposit(25)
b.withdraw(1)

print("The balance of the bank account is now" + str(b.balance))