class Product:
    def __init__(self, price):
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)

    def checkout(self, printer):
        return printer.print_receipt(self.total())  # Delegate receipt formatting.


class ReceiptPrinter:
    def print_receipt(self, total):
        return f"Total: {total:.2f}"


cart = ShoppingCart()
cart.add(Product(5))
cart.add(Product(7.5))
print(cart.checkout(ReceiptPrinter()))
