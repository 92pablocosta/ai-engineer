class MemoryStorage:
    def save(self, text):
        return f"memory: {text}"


class ConsoleStorage:
    def save(self, text):
        return f"console: {text}"


def save_document(storage, text):
    return storage.save(text)  # Both classes satisfy the same informal contract.


print(save_document(MemoryStorage(), "note"))
print(save_document(ConsoleStorage(), "note"))
