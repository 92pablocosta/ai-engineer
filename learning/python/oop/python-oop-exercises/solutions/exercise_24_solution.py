class BrokenStorage:
    pass


def save_document(storage, text):
    return storage.save(text)


try:
    save_document(BrokenStorage(), "note")
except AttributeError:
    # The required informal contract is a save(text) method.
    print("storage must provide save: AttributeError")
