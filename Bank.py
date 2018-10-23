class Account:
    def __init__(self, name, balance, min_balance) :

        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Not enough money!")

    def statement(self):
        print("Account Balance : {}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)
    def __str__(slef):
        return "{}'s Current Account".format(slef.name)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)
    def __str__(slef):
        return "{}'s Savings Account".format(slef.name)
