class Product:
    def __init__(self, price):
        self._price = price

    def apply_discount(self, percent):
        pass

    def get_price(self):
        return self._price


product = Product(100)
# TODO: apply 20%, then 150%, and print each result and price.
