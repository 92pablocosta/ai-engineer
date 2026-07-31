class Account:
    def __init__(self, owner):
        self.owner = owner

    def show_owner(self):
        return f"Owner: {self.owner}"


account = Account("Ada")
print(account.show_owner())
