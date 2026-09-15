class InsufficientFunds(Exception):
    pass


class BankAccount:
    count = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.count += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFunds(f"balance {self.balance} < {amount}")
        self.balance -= amount
        return self.balance

    def transfer(self, other, amount):
        self.withdraw(amount)  # raises before other is touched
        other.deposit(amount)

    def __repr__(self):
        return f"BankAccount({self.owner!r}, {self.balance})"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return (self.owner, self.balance) == (other.owner, other.balance)
