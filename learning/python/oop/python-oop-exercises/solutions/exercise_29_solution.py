class ReadingTracker:
    def __init__(self):
        self._pages_read = 0

    def read_pages(self, amount):
        if amount > 0:
            self._pages_read += amount  # Invalid changes are ignored.

    def get_pages_read(self):
        return self._pages_read


tracker = ReadingTracker()
tracker.read_pages(15)
print(tracker.get_pages_read())
tracker.read_pages(-2)
print(tracker.get_pages_read())
