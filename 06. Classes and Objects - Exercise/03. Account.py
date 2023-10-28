class Account:
    def __init__(self, id: int, name: str, balance: float = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def debit(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
