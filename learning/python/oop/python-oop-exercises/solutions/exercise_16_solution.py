class LibraryItem:
    def __init__(self):
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_item(self):
        self.is_borrowed = False


class Magazine(LibraryItem):
    pass


magazine = Magazine()
magazine.borrow()
print(magazine.is_borrowed)
magazine.return_item()
print(magazine.is_borrowed)
