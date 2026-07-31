class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        pass  # TODO: validate amount and available balance.

    def get_balance(self):
        return self._balance


account = BankAccount(100)
# TODO: withdraw 30, try 80, and print results and balance.
