class Product:
    def __init__(self, price):
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self, product):
        pass

    def total(self):
        pass

    def checkout(self, printer):
        pass


class ReceiptPrinter:
    def print_receipt(self, total):
        pass


# TODO: add products costing 5 and 7.5, then checkout.
