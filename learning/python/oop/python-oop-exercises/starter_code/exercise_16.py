class LibraryItem:
    def __init__(self):
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_item(self):
        self.is_borrowed = False


class Magazine:
    pass  # TODO: inherit from LibraryItem.


# TODO: borrow then return a magazine and print is_borrowed each time.
