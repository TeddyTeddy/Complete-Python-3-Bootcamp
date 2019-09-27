import datetime
import pytz


class Account2(object):

    @staticmethod
    def _current_time():  # non-public
        utc_time = datetime.datetime.now()
        return pytz.utc.localize(utc_time)

    def __init__(self, owner, balance):
        self._owner = owner  # A single underscore '_', a light indication of non-public instance attribute
        self._transaction_list = []
        self.__balance = 0  # double underscore '_' makes Python apply name mangling to the variable: _Account2__balance
        self.deposit(balance)  # makes a negative balance check
        print(f'Account for {self._owner} is opened with balance {self.__balance}')

    def deposit(self, amount):
        if amount < 0:
            raise AssertionError
        self.__balance += amount
        self._transaction_list.append((Account2._current_time(), amount))
        print(f'Deposit {amount} accepted')

    def withdraw(self, amount):
        if self.__balance < amount:
            print(f'Funds Unavailable! Balance {self.__balance}, Amount {amount}')
            raise AssertionError
        self.__balance -= amount
        self._transaction_list.append((Account2._current_time(), -amount))
        print(f'Withdrawal {amount} accepted')

    def show_balance(self):
        print(f'Balance is {self.__balance}')

    def show_transactions(self):
        for date, amount in self._transaction_list:  # tuple unpacking
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = 'withdrawn'
                amount *= -1
            print(f'{amount:6} {trans_type} on {date} (local time was {date.astimezone()}')

    def __str__(self):
        return f'Account owner: {self._owner}\nAccount balance: {self.__balance}'


tim = Account2('Tim', 0)
tim.show_balance()
tim.deposit(1000)
tim.withdraw(500)
tim.show_transactions()

steph = Account2('Steph', 800)
steph.deposit(100)
steph.withdraw(200)
steph.show_transactions()

# to show that _current_time() is indeed in the namespace of Account2 class
print(Account2.__dict__)
print(tim.__dict__)
print(steph.__dict__)
