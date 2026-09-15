"""
Problem: Bank account class
Difficulty: Warm-up | Topic: classes, __init__, __repr__, __eq__, custom exceptions

Implement:

class InsufficientFunds(Exception): a custom exception.

class BankAccount:
  BankAccount(owner: str, balance: int = 0)
  .deposit(amount) -> new balance. Raise ValueError if amount <= 0.
  .withdraw(amount) -> new balance. Raise ValueError if amount <= 0,
                       InsufficientFunds if amount > balance.
  .transfer(other, amount) -> None. Withdraw from self, deposit into other.
                       If the withdrawal fails, other must be untouched.
  repr(acct) == "BankAccount('alice', 100)"
  Two accounts are == when owner and balance match.
  BankAccount.count is a class attribute: number of accounts ever created.

Hints:
1. Increment the class attribute with BankAccount.count += 1 inside __init__ (not self.count).
2. Use f"{self.owner!r}" to get the quotes in repr.
3. __eq__ should return NotImplemented for non-BankAccount others.
"""


class InsufficientFunds(Exception):
    pass


class BankAccount:
    count = 0

    def __init__(self, owner: str, balance: int = 0):
        raise NotImplementedError

    def deposit(self, amount: int) -> int:
        raise NotImplementedError

    def withdraw(self, amount: int) -> int:
        raise NotImplementedError

    def transfer(self, other: "BankAccount", amount: int) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    a = BankAccount("alice", 100)
    b = BankAccount("bob")
    assert BankAccount.count == 2
    assert a.deposit(50) == 150
    assert a.withdraw(30) == 120
    assert repr(a) == "BankAccount('alice', 120)"
    assert repr(b) == "BankAccount('bob', 0)"
    try:
        a.withdraw(1000)
        assert False
    except InsufficientFunds:
        pass
    try:
        a.deposit(-5)
        assert False
    except ValueError:
        pass
    a.transfer(b, 20)
    assert a.balance == 100 and b.balance == 20
    try:
        b.transfer(a, 999)
        assert False
    except InsufficientFunds:
        pass
    assert a.balance == 100 and b.balance == 20
    assert BankAccount("x", 5) == BankAccount("x", 5)
    assert BankAccount("x", 5) != BankAccount("y", 5)
    assert BankAccount.count == 6
    print("ok")
