class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Command.

    def get_balance(self):
        return self.balance  # Query.


wallet = Wallet(10)
wallet.deposit(25)
print(wallet.get_balance())
