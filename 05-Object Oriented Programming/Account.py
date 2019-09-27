class Account(object):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise AssertionError
        self.balance += amount
        print('Deposit accepted')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Funds Unavailable!')
            raise AssertionError
        self.balance -= amount
        print('Withdrawal accepted')

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

