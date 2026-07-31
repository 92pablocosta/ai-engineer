class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount  # Update only after validation.
        return True

    def get_balance(self):
        return self._balance


account = BankAccount(100)
print(account.withdraw(30))
print(account.withdraw(80))
print(account.get_balance())
