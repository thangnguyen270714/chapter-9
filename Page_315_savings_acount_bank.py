"""
Author: Nguyen Duc Thang
Date: 1/11/2021
Program: Page_315_savings_acount_bank.py
Problem: This module defines the SavingsAccount class.

"""
class SavingsAccount(object):
    """This class represents a savings account
    with the owner's name, PIN, and balance."""
    RATE = 0.02

    def __init__(self,name,pin,balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result = 'Name ' + self.name + "\n"
        result += 'Pin ' + self.pin + "\n"
        result += 'Balance ' + str(self.balance) + "\n"
        return result

    def getbalance(self):
        """Returns the current balance."""
        return self.balance

    def getname(self):
        """Returns the current name."""
        return self.name

    def getpin(self):
        """Returns the current PIN."""
        return self.pin

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

class Bank(object):
    def __init__(self):
        self.accounts = {}

    def __str__(self):
        """Return the string rep of the entire bank."""
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        """Makes and returns a key from name and pin."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an account with name and pin as a key."""
        key = self.makeKey(account.getName(),
                           account.getPin())
        self.accounts[key] = account
    def remove(self, name, pin):
        """Removes an account with name and pin as a key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns an account with name and pin as a key
        or None if not found."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes interest for each account and
        returns the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computelnterest()
        return total

def test_bank():
    bank = Bank()
    bank.add(SavingsAccount("Jackson", "2991", 4000.00))
    bank.add(SavingsAccount("Emma", "2997", 7000.00))
    print(bank)
    print(f"bank.computeInterest: ", bank.computeInterest())


if __name__=='__main__':
    test_bank()