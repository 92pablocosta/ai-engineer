class Product:
    def __init__(self, price):
        self._price = price

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            return False
        self._price *= 1 - percent / 100
        return True

    def get_price(self):
        return self._price


product = Product(100)
print(product.apply_discount(20))
print(product.get_price())
print(product.apply_discount(150))
print(product.get_price())
