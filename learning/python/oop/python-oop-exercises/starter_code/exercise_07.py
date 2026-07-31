class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return f'${self.balance}'


wallet = Wallet(10)
# TODO: deposit 25 and print the balance.
wallet.deposit(25)
print(wallet.get_balance())
